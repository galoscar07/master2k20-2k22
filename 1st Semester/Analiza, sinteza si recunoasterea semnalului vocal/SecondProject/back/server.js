const express = require('express');
const fs = require('fs');
const readline = require('readline');
const bodyParser = require("body-parser");
const {google} = require("googleapis");


const app = express();
const port = process.env.PORT || 88;
const SCOPES = ['https://www.googleapis.com/auth/spreadsheets'];
const TOKEN_PATH = 'token.json';



app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "OPTIONS, GET, POST");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

function authorize(credentials, callback, body = null) {
    const {client_secret, client_id, redirect_uris} = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(
        client_id, client_secret, redirect_uris[0]);
    fs.readFile(TOKEN_PATH, (err, token) => {
        if (err) return getNewToken(oAuth2Client, callback, body);
        oAuth2Client.setCredentials(JSON.parse(token));
        return callback(oAuth2Client, body);
    });
}

function getNewToken(oAuth2Client, callback, body = null) {
    const authUrl = oAuth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
    });
    console.log('Authorize this app by visiting this url:', authUrl);
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    rl.question('Enter the code from that page here: ', (code) => {
        rl.close();
        oAuth2Client.getToken(code, (err, token) => {
            if (err) return console.error('Error while trying to retrieve access token', err);
            oAuth2Client.setCredentials(token);
            // Store the token to disk for later program executions
            fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
                if (err) return console.error(err);
                console.log('Token stored to', TOKEN_PATH);
            });
            return callback(oAuth2Client, body);
        });
    });
}


app.get("/data", function (req, res) {

    fs.readFile('credentials.json', (err, content) => {
        if (err) return console.log('Error loading client secret file:', err);
        authorize(JSON.parse(content), datapull);
    });

    function datapull(auth) {
        const sheets = google.sheets({version: 'v4', auth});
        var result = sheets.spreadsheets.values.get({
            spreadsheetId: '10p9YFkCysZTcu29m2jiCIh7kcqyuM2ZQ4Vc1NZsl8Tg',
            range: 'Foaie1!A2:H',
        }, (err, response) => {
            if (err) return console.log('The API returned an error: ' + err);
            const rows = response.data.values;
            res.send({rows: rows})
        });
    }
});

app.use(bodyParser.json())
app.post("/data", function (request, response) {
    const data = request.body

    fs.readFile('credentials.json', (err, content) => {
        if (err) return console.log('Error loading client secret file:', err);
        authorize(JSON.parse(content), datapush, data);
    });

    function datapush(auth, body) {
        const sheets = google.sheets({version: 'v4', auth});

        let resource = {
            values: [
                [body.limba, body.nrCuvinteGresite, body.nrCuvinte, body.nrCuvinteInlocuite, body.nrCuvinteNoiIntroduse, body.nrCuvinteSterse, body.di, body.dt]
            ]
        }

        sheets.spreadsheets.values.append({
            spreadsheetId: '10p9YFkCysZTcu29m2jiCIh7kcqyuM2ZQ4Vc1NZsl8Tg',
            range: 'Foaie1!A2:H',
            valueInputOption: 'RAW',
            resource,
        }, (err, result) => {
            if (err) {
                console.log(err);
                response.end('An error occurd while attempting to save data. See console output.');
            } else {
                const responseText = `${result.data.updates.updatedCells} cells appended.`;
                console.log(responseText);
                response.end(responseText);
            }
        });
    }

})

app.listen(port);
console.log(`Server started. Listening on port ${port}`);
