import React from "react";
import './LogIn.scss'

export default class LogIn extends React.Component {
    render() {
        return (
            <div className='page-authentication page-login'>
                <div className='rounded-card-login'>
                    <div className='form-title'>Log In</div>
                    <div className='sub-form-title'>Connect to your Virtual Reality account.</div>

                    <div className='action-button login-button'>Log In</div>
                </div>
            </div>
        )
    }
}
