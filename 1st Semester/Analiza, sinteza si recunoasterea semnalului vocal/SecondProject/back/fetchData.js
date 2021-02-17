const fetchGoogleSheetTab = require('./fetchGoogleSheetTab')

async function fetchData() {
    try {
        console.log('2')
        await fetchGoogleSheetTab.fetchGoogleSheetTab(0).then((res) => {
            return(res);
        });
    } catch (err) {
        console.log(err);
        return false;
    }
}

module.exports={fetchData}
