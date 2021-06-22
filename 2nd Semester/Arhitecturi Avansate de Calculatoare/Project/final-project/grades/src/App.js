import React from "react";
import {Route, BrowserRouter as Router, Switch, Redirect} from "react-router-dom";

import './App.scss';

import LogIn from "./pages/LogIn";
import Homepage from "./pages/Homepage";
import Statistics from "./pages/Statistics";


const checkAuth = () => {
    // Verify if the user is authenticated or not
    const token = localStorage.getItem('access_token')
    return !!token
}

const AuthenticatedRoutes = ({component: Component, ...rest}) => (
    <Route {...rest} render={(props) => (
        checkAuth() ? (
            <Component {...props} />
        ) : (
            <Redirect to={{pathname: '/login'}}/>
        )
    )}
    />
)

function App() {
    return (
        <Router>
            <Switch>
                <Route exact path={'/login'} component={LogIn}/>
                <AuthenticatedRoutes exact path={'/'} component={Homepage}/>
                <AuthenticatedRoutes exact path={'/statistics'} component={Statistics}/>
            </Switch>
        </Router>
    );
}

export default App;
