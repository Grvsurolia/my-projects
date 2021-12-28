// CAMPAIGN SETTING
import React, { Component } from 'react'
import { connect } from 'react-redux'
import { Container, Row, Col, Button, Alert } from 'reactstrap'
import Form from 'reactstrap/lib/Form'
import Campaign_details from "../../../views/pages/Campaing/Campaign_details"
import { CampaignLeadCatcherAction, CampaignLeadGetAction, CampaignLeadDeleteAction, CampaignLeadUpdateAction } from "../../../redux/action/CampaignAction"

// export default function Setting() {
export class CampSetting extends Component {
    constructor(props) {
        super(props)
        this.state = {
            recipientsData: '',
            num: '',
            specific_link: null,
            isOpen: false,
            show: false,
            hide: false
        }
    }
    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value,
            show: true,
        })
    }
    handleSubmit = (e) => {
        e.preventDefault()
        this.setState({ isOpen: true })
        if (!this.state.recipientsData || !this.state.num) {
            alert('Fill all information')
        }
        var id = this.props.history.location.state && this.props.history.location.state.id
        if (this.props.lead && this.props.lead.campaign) {
            //put
            const updateLeadData = {
                leadcatcher_recipient: this.state.recipientsData,
                of_times: this.state.num,
                specific_link: this.state.specific_link
            }
            const getId = this.props.lead.id;
            this.props.CampaignLeadUpdateAction(getId, id, updateLeadData)
        }
        else {
            //post
            const leadData = {
                leadcatcher_recipient: this.state.recipientsData,
                of_times: this.state.num,
                specific_link: this.state.specific_link
            }
            this.props.CampaignLeadCatcherAction(id, leadData)

        }
    }
    componentDidMount() {
        const id = this.props.history.location.state && this.props.history.location.state.id;
        this.props.CampaignLeadGetAction(id)
    }
    // this.props.CampaignLeadUpdateAction(id)
    componentWillReceiveProps(preProps, nextProps) {
        console.log({
            preProps, nextProps
        })
    }
    leadDeleteAction(id) {
        this.props.CampaignLeadDelete(id)
        alert('You want to delete this leadCatcher')
    }
    render() {
        const id = this.props.history.location.state && this.props.history.location.state.id;
        const { lead, leadData } = this.props;
        return (
            <>
                <div>
                    <Container fluid>
                        <Row>
                            <Campaign_details id={this.props.history.location.state && this.props.history.location.state.id} />
                        </Row>
                        <Row className='mb-5 mt-5'>
                            <Col md={4} >
                                <div className='boxShadow setting_div'>
                                    <div className='p-3 settingUnderline'>
                                        <h3 className='display-4'>Sending Account</h3>
                                        <label className='filter_app'>Who should leads be assigned to ?</label><br></br>
                                        <select className='filter_select_prospect'>
                                            <option value='one'>Me</option>
                                        </select>
                                        <p className='mt-3'>When does a recipient become a lead?</p>
                                        <Row className='mt-3'>
                                            <Col>
                                                <label className='filter_app'>Who should leads be assigned to ?</label><br></br>
                                                <select className='filter_select_prospect mt-3'>
                                                    <option value='one'>Me</option>
                                                </select>
                                            </Col>
                                        </Row>
                                    </div>
                                    <div className='p-3'>
                                        <button className=' btn startBtn'>SAVE</button>
                                    </div>
                                </div>
                            </Col>
                            <Col md={4} >
                                <Form onSubmit={this.handleSubmit}>
                                    <div className='boxShadow setting_div'>
                                        <div className='p-3 settingUnderline'>
                                            <h3 className='display-4'>Lead Catcher</h3>
                                            <Row>
                                                <Col>
                                                    <label className='filter_app'>Who should leads be assigned to ?</label><br></br>
                                                    <select className='filter_select_prospect mt-3'>
                                                        <option value='one'>Me</option>
                                                    </select>
                                                </Col>
                                            </Row>
                                            <Row>
                                                <Col>
                                                    <label className='filter_app mt-3'>When does a recipient become a lead?</label><br></br>
                                                    <Row className='mt-3'>
                                                        <Col md={6} className='mt-4'>
                                                            <label>Recipients</label>
                                                            <select name='recipientsData' onChange={this.handleChange} value={this.state.recipientsData} className='filter_select_prospect mt-3' required>
                                                                <option value='' selected disabled hidden>{lead.leadcatcher_recipient}</option>
                                                                <option value='replies'>Replies</option>
                                                                <option value='open'>Opens</option>
                                                                {/* <option value='click_any_link'>Click any link</option>
                                                                <option value='clicks_specific_link' >Click specific link</option> */}
                                                            </select>
                                                        </Col>
                                                        {/* {this.state.hide && <div className='mt-3' style={{width:"100%"}}><input className='form-control w-100' type='url'></input></div>} */}
                                                        <Col md={5} className='mt-4'>
                                                            <label>#Of times</label>
                                                            <input type='number' name="num" onChange={this.handleChange} value={this.state.num} className='filter_select_prospect mt-2' required placeholder={lead.of_times} />
                                                        </Col>
                                                        {/* <Col md={1} className='mt-5' style={{ display: 'flex', flexDirection: 'row-reverse' }}>
                                                            <span onClick={() => { this.leadDeleteAction(lead.id) }} style={{ fontSize: '20px', cursor: 'pointer' }}><i className="fa fa-trash"></i></span>
                                                        </Col> */}
                                                    </Row>
                                                    <Row>
                                                        {this.state.recipientsData === 'clicks_specific_link' && <div className='mt-3 w-100 p-2'><input name='specific_link' onChange={this.handleChange} value={this.state.specific} className='form-control w-100' type='url'></input></div>}
                                                    </Row>
                                                </Col>
                                            </Row>
                                        </div>
                                        <Row className='ml-2'>
                                            <div className='p-3' style={{ display: 'flex' }}>
                                                <Button type='submit' className=' btn startBtn'>SAVE</Button>
                                                {this.state.show && <button onClick={() => { this.setState({ show: false }) }} className=' btn sequence_btn'>CANCEL</button>}
                                            </div>
                                        </Row>
                                    </div>
                                </Form>
                            </Col>
                        </Row>
                    </Container>
                </div>
                {/* <div style={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'flex-end', position: 'absolute', bottom: 0, right: 0 }}> */}
                {/* <Alert className="alert_" onClick={() => { this.setState({ isOpen: !this.state.isOpen }) }} isOpen={this.state.isOpen} color="success">{leadData.message}</Alert> */}
                {/* </div> */}
            </>
        )
    }
}
const mapStateToProps = (state) => {
    return {
        lead: state.LeadGetReducer && state.LeadGetReducer.leadGetData,
    };
};
const mapDispatchToProps = (dispatch) => ({
    CampaignLeadCatcherAction: (id, leadData) => { dispatch(CampaignLeadCatcherAction(id, leadData)) },
    CampaignLeadDelete: (id) => { dispatch(CampaignLeadDeleteAction(id)) },
    CampaignLeadGetAction: (id) => { dispatch(CampaignLeadGetAction(id)) },
    CampaignLeadUpdateAction: (getId, id, updateLeadData) => { dispatch(CampaignLeadUpdateAction(getId, id, updateLeadData)) }

});

export default connect(mapStateToProps, mapDispatchToProps)(CampSetting)
