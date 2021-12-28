import { history } from "../.."
import {

    FAILURE_REGISTER,
    REQUEST_FOR_REGISTER,
    SUCCESS_REGISTER,
    FAILURE_LOGIN,
    REQUEST_FOR_LOGIN,
    SUCCESS_LOGIN,  
} from "../actionType/actionType"

import Api from "../api/api"

// Register
export const requestForRegister = () => {
    return {
        type: REQUEST_FOR_REGISTER,
    }
}

export const registerSuccess = (user) => {
    console.log(user, 'data')
    return {
        type: SUCCESS_REGISTER,
        user
        
    }
}
export const registerFailure = (payload) => {
    return {
        type: FAILURE_REGISTER,
        payload
    }
}

// login
export const requestForLogin = () => {
    return {
        type: REQUEST_FOR_LOGIN,
    }
}
export const LoginSuccess = (Loginuser) => {
    console.log(Loginuser, 'data')
    return {
        type: SUCCESS_LOGIN,
        Loginuser
    }
}
export const loginFailure = (payload) => {
    return {
        type: FAILURE_LOGIN,
        payload
    }
}

// register action
export const RegisterAction = (user) => {
    return function (dispatch) {
        dispatch(requestForRegister(user))
        Api.RegisterApi(user).then(result => {
            console.log( 'registerSuccess',result.data)
            dispatch(registerSuccess(result.data))
            history.push('/app/auth/login')
        }).catch(err => {
            err.response.data.email&&  dispatch(registerFailure(err.response.data.email))
            console.log(err.response.data.email)
        })
    }
}

// login action
export const LoginAction = (Loginuser) => {
    return function (dispatch) {
        dispatch(requestForLogin(Loginuser))
        Api.LoginApi(Loginuser).then(result => {
            const token = result.data.token;
            localStorage.setItem('access_token', token)
            dispatch(LoginSuccess(result.data))
            history.push('/app/admin/dashboard')
        }).catch(err => {
            dispatch(loginFailure(err.response.data.non_field_errors&&err.response.data.non_field_errors[0]))
        })
    }
}
