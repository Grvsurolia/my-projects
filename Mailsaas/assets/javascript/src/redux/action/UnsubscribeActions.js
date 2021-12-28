import {
    SUCCESS_FETCH_UNSUBSCRIPTION,
    REQUEST_FOR_UNSUBSCRIBE_WITH_CSV,
    SUCCESS_UNSUBSCRIBE_WITH_CSV,
   FAILURE_UNSUBSCRIBE_WITH_CSV

} from "../actionType/actionType"
import Api from "../api/api";
import { CampaignPeopleAction } from "./CampaignAction";

export const requestUserUnsubscribeWithCsv = () => {
    return {
        type: REQUEST_FOR_UNSUBSCRIBE_WITH_CSV,
    }
}
export const successUserUnsubscribeWithCsv = () => {
    return {
        type: SUCCESS_UNSUBSCRIBE_WITH_CSV,
    }
}
export const failureUserUnsubscribeWithCsv = () => {
    return {
        type:FAILURE_UNSUBSCRIBE_WITH_CSV,
    }
}
export const successFetchUnsubscribe = (payload) => {
    return {
        type: SUCCESS_FETCH_UNSUBSCRIPTION,
        payload
    }
}

export const fetchUnsubscribeAction =() => {
    return function (dispatch) {
        console.log("hiii")
        const token = localStorage.getItem('access_token')
        Api.fetchUnsbcribed(token).then((response) => {
            console.log(response, "unsubscrive")
            dispatch(successFetchUnsubscribe(response.data));
        }).catch((err) => {
            console.log(err, 'err')
        })
    }
}

export const deleteUnsubscribeUsersAction = (data) => {
    return function (dispatch) {
        const token = localStorage.getItem('access_token')
        Api.deleteUnsbcribed(data, token).then((response) => {
            console.log(response,"seudfdfgfhfdhdfgh")
            dispatch(fetchUnsubscribeAction())
        }).catch((err) => {
            console.log(err, 'err')
        })
    }
}

export const unsubscribeUsersWithCsvAction = (data) => {
    return function (dispatch) {
        const token = localStorage.getItem('access_token')
        dispatch(requestUserUnsubscribeWithCsv)
        Api.unsubscribeUsersWithCsvApi(data, token).then((response) => {
            dispatch(fetchUnsubscribeAction())
        }).catch((err) => {
            console.log(err, 'err')
        })
    }
}
export const unsubscribeUsersWithEmailAction = (data) => {
    return function (dispatch) {
        console.log("datadatadata",data)
        const token = localStorage.getItem('access_token')
        Api.unsubscribeUsersWithEmailApi(data,token).then((response) => {
            dispatch(fetchUnsubscribeAction())
        }).catch((err) => {
            console.log(err, 'err')
            dispatch(failureUserUnsubscribeWithCsv())
        })
    }
}
