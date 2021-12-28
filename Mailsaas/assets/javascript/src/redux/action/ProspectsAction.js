import {
    FETCH_PROSPECTS,
    SUCCESS_FETCH_PROSPECTS,
    FAILURE_FETCH_PROSPECTS,
    SUCCESS_FETCH_ONCLICK_PROSPECTS,
    DELETE_PROSPECT
} from "../../redux/actionType/actionType"

import Api from "../api/api"

// GET PROSPECT 
export const FetchProspects = () => {
    return {
        type: FETCH_PROSPECTS
    }
}
export const FetchProspectsSuccess = (prospectData) => {
    return {
        type: SUCCESS_FETCH_PROSPECTS,
        prospectData
    }
}
export const FailureProspects = () => {
    return {
        type: FAILURE_FETCH_PROSPECTS
    }
}

// GET ONCLICK PROSPECT
export const FetchOnclickProspectsSuccess = (prospectOnclickData) => {
    return {
        type: SUCCESS_FETCH_ONCLICK_PROSPECTS,
        prospectOnclickData
    }
}

// DELETE PROPSPECT


export const ProspectActionData = (id) => {
    return function (dispatch) {
        const token = localStorage.getItem('access_token')
        dispatch(FetchProspects(token))
        Api.CampaignProspects(token,id).then(result => {
            console.log(result.data)
            dispatch(FetchProspectsSuccess(result.data))
            console.log("checking prospect data:", result.data)
        }).catch(err => {
            console.log(err)
        })
    }
}

// ACTION FOR ONCLICK PROSPECT
export const OnclickProspectActionData = (data) => {
    // console.log('OnclickProspectActionData ',data);
    return function (dispatch) {
        const token = localStorage.getItem('access_token')
        // const datat=localStorage.getItem('pid')
        Api.CampaignOnclickProspects(data,token).then(result => {
            dispatch(FetchOnclickProspectsSuccess(result.data[0]))
            console.log("checking onclick prospect data:", result.data[0])
        }).catch(err => {
            console.log(err)
        })
    }
}
export const ProspectUnsubscribeAction = (id) => {
    return function (dispatch) {
        const token = localStorage.getItem('access_token')
        Api.ProspectsUnsubscribe(id,token).then(result => {
           dispatch(ProspectActionData())
        }).catch(err => {
            console.log(err)
        })
    }
}


export const deleteProspectAction = (data) => {
    // console.log('deleteProspectActiondata[0]:',data[0]);
    return function (dispatch) {
        const token = localStorage.getItem('access_token')
        // const pid=localStorage.setItem('pid')
        Api.deleteProspects(data, token).then((response) => {
            console.log('2222 pagala gya hai kya',data,response);
            dispatch(ProspectActionData(data[0]))
        }).catch((err) => {
            console.log(err, 'err')
        })
    }
}

