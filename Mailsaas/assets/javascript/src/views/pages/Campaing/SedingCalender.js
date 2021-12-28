import React, { Component } from 'react'
import { Container, Row, Col, Form, Label, Input, Dropdown, DropdownToggle, DropdownMenu, DropdownItem, Table, Button, Card } from 'reactstrap'
import CardBody from 'reactstrap/lib/CardBody'
import CardFooter from 'reactstrap/lib/CardFooter'
import CardHeader from 'reactstrap/lib/CardHeader'
import { connect } from 'react-redux'
import { GetScheduleAction, ScheduleUpdateAction } from '../../../redux/action/ScheduleAction'
import {MailGetDataAction} from '../../../redux/action/MailSenderAction'
export class SendingCalender extends Component {
  constructor(props) {
    super(props)
    var days = ['mo', 'tu', 'we', 'th', 'fr', 'st','su'];
    this.state = {
      show: true,
      hide: false,
      MailAccounts: '',
      BlockDays: [],
      Date: '',
      StartTime: '',
      EndTime: '',
      Timezone: '',
      MaxEmails: '',
      Strategy: '',
      Minutes: '',
      MaxEmailSend: '',
      days: days
    }
    // console.log('))))))))))))===========>',this.state.BlockDaysssssssss)
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  componentDidMount() {
    this.props.GetScheduleAction()
    this.props.MailGetDataAction()
  }

  handleChange = (e) => {
    console.log("called",e)
    this.setState({
      [e.target.name]: e.target.value
    })
  }
  handleBlockDays = (data) => {
    console.log(data)
  }
  handleSubmit = (event) => {
    event.preventDefault();
    console.log(event)
    const updatedataschedule = {
      mail_account: this.state.MailAccounts,
      block_days: this.state.BlockDays,
      date: this.state.Date,
      start_time: this.state.StartTime,
      end_time: this.state.EndTime,
      time_zone: this.state.Timezone,
      max_email: this.state.MaxEmails,
      strategy: this.state.Strategy,
      mint_between_sends: this.state.Minutes,
      max_email_send: this.state.MaxEmailSend
    }
    this.props.ScheduleUpdateAction(updatedataschedule)
    this.setState({ hide: !this.state.hide, show: !this.state.show })
  }
  edit = (ScheduleData) => {
    this.setState({
      MailAccounts: ScheduleData.mail_account,
      BlockDays: ScheduleData.block_days,
      Date: ScheduleData.date,
      StartTime: ScheduleData.start_time,
      EndTime: ScheduleData.end_time,
      Timezone: ScheduleData.time_zone,
      MaxEmails: ScheduleData.max_email,
      Strategy: ScheduleData.strategy,
      Minutes: ScheduleData.mint_between_sends,
      MaxEmailSend: ScheduleData.max_email_send,
      show: !this.state.show,
      hide: !this.state.hide
    })
  }
  render() {
    const { ScheduleData,mailGetDat } = this.props;
    console.log('ScheduleData', ScheduleData)
    return (
      <div>
        <div className='campaign_navbar' >
          <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>SendingCalendar</h1>
          <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i className="fa fa-question-circle-o" aria-hidden="true"></i></p>
        </div>
        <div>
          {!this.state.hide &&
            <Container style={{ marginLeft: "0px" }}>
              <Row className='mt-3'>
                <Col md="4">
                  <Card>
                    <CardHeader style={{ border: "none" }}>
                      <select className='scalender_filter_select'>
                        <option>{this.props.mailGetDat &&this.props.mailGetDat.map((e,i)=>{return e.email}) }</option>
                      </select>
                    </CardHeader>
                    <CardBody>
                      <div >
                          {this.state.days.map((item, index) => {
                            return <span className='blockdays' key={index}>{item}</span>
                          })}
                      </div>
                      <div style={{ fontSize:"12px",marginTop:'5px'}}>
                        <div className="calender_details">
                          <span className='calendedata'> {ScheduleData && ScheduleData.start_time}</span> to <span className='calendedata'>{ScheduleData && ScheduleData.end_time} {ScheduleData && ScheduleData.time_zone}</span> Send no more than <span className='calendedata'>{ScheduleData && ScheduleData.max_email}</span> emails per day Space emails out over the day Pause  <span className='calendedata'>{ScheduleData && ScheduleData.mint_between_sends}</span> minutes between sends  Send at least <span className='calendedata'>{ScheduleData && ScheduleData.max_email_send}</span> emails at a time </div> </div>
                      <div>
                        <span style={{ fontSize: "10px" }}><i className="fa fa-question-circle-o" aria-hidden="true"></i></span>
                        <span style={{ fontSize: "10px" }}>about these settings</span>
                      </div>
                    </CardBody>
                    <CardFooter >
                      <Button className="b1" onClick={() => this.edit(ScheduleData)}>Edit Rules</Button>
                    </CardFooter>
                  </Card>
                </Col>
              </Row>
            </Container>}
          {!this.state.show && <Container fluid>
            <Form onSubmit={this.handleSubmit}>
              <Row className='mt-3 mb-5'>
                <Col md='4' style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>
                  <div style={{ margin: '17px 0px 24px 24px' }}>
                    <div className='dv1'>
                      <Row> <label>Mail account</label></Row>
                      <Row >
                        <select className='teamname-input'>
                        <option>{this.props.mailGetDat &&this.props.mailGetDat.map((e,i)=>{return e.email}) }</option>
                        </select>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>Blocked out days</label>
                      </Row>
                      <Row>
                        <div>
                          {this.state.days.map((item, index) => {
                            // console.log('blockdays index:', item, index);
                            return <input className='blockdays' onClick={() => this.handleBlockDays(index)} name='BlockDays' value={this.state.BlockDays} key={index}></input>
                          })}
                        </div>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>Start time</label>
                      </Row>
                      <Row>
                        <input className='teamname-input' name='StartTime' onChange={this.handleChange} value={this.state.StartTime}></input>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>End time</label>
                      </Row>
                      <Row>
                        <input className='teamname-input' name="EndTime" onChange={this.handleChange} value={this.state.EndTime}></input>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>TimeZone</label>
                        <select className='teamname-input'>
                          <option>{this.state.Timezone}</option>
                        </select>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <Row>
                          <Col style={{ display: "flex" }}>
                            <label>Max emails per day</label>
                          </Col>
                        </Row>
                        <input type='number' className='teamname-input' name='MaxEmails' onChange={this.handleChange} value={this.state.MaxEmails}></input>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>Strategy</label>
                        <select className='teamname-input'>
                          <option>{this.state.Strategy}</option>
                        </select>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>Minutes between sends</label>
                      </Row>
                      <Row>
                        <input type='number' className='teamname-input' name='Minutes' onChange={this.handleChange} value={this.state.Minutes} ></input>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>Minimum emils tosend at a time</label>
                      </Row>
                      <Row>
                        <input type='number' className='teamname-input' name='MaxEmailSend' onChange={this.handleChange} value={this.state.MaxEmailSend}></input>
                      </Row>
                      <Row className='mt-4' style={{ display: 'flex', flexDirection: 'column' }}>
                        <label>Maximum emils to send at a time</label>
                      </Row>
                      <Row>
                        <input type='number' className='teamname-input' name='MaxEmailSend' onChange={this.handleChange} value={this.state.MaxEmailSend}></input>
                      </Row>
                      <Row className='mt-5'>
                        <button className='savebutton' type='Submit' onSubmit={this.handleSubmit}>save</button>
                        <button className='savebutton' onClick={(e) => { e.preventDefault(), this.setState({ hide: !this.state.hide, show: !this.state.show }) }}>CANCEL</button>
                      </Row>
                    </div>
                  </div>
                </Col>
              </Row>
            </Form>
          </Container>}
          {/* {!this.state.hide && <div className="calender_box" style={{ backgroundColor: "transparant", width: "100%", display: "flex", flexDirection: "row" }}>
            <div className="su_box">
              <p>{ScheduleData && ScheduleData.date}</p>
            </div>
            <div className="mo_box">
              <p>z</p>
            </div>
            <div className="tu_box">
              <p>f</p>
            </div>
            <div className="we_box">
              <p>as</p>
            </div>
            <div className="th_box">
              <p>a</p>
            </div>
            <div className="fr_box">
              <p>w</p>
            </div>
            <div className="sa_box">
              <p>w</p>
            </div>
          </div>
          } */}
        </div>
      </div>
    )
  }
}
const mapStateToProps = (state) => {
  console.log('checking mail data', state.MailGetDataReducer.mailGetData && state.MailGetDataReducer.mailGetData.map((e,i)=>{return e.email}))
  return {
    ScheduleData: state.ScheduleGetDataReducer.ScheduleGetData,
    mailGetDat: state.MailGetDataReducer.mailGetData 
  }
}
const mapDispatchToProps = dispatch => ({
  GetScheduleAction: ScheduleGetData => { dispatch(GetScheduleAction(ScheduleGetData)) },
  ScheduleUpdateAction: updatedataschedule => { dispatch(ScheduleUpdateAction(updatedataschedule)) },
  MailGetDataAction: () => { dispatch(MailGetDataAction()) }
})
export default connect(mapStateToProps, mapDispatchToProps)(SendingCalender)
