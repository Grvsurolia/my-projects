import React, { Component } from 'react'
import LeadCatchermodel from "./LeadCatchermodel"
import { connect } from 'react-redux'
import { CampaignLeadViewAction, CampaignOverviewAction } from "../../../redux/action/CampaignAction";
import { Container, Row, Col, Input, Modal, ModalHeader, ModalBody, Table } from 'reactstrap'

class LeadCatcher extends Component {
  constructor() {
    super()
    this.state = {
      modal: false

    }
  }
  componentDidMount() {
    this.props.CampaignLeadViewAction()
  }
  toggle = () => {
    this.setState({ modal: !this.state.modal })
  }
  render() {
    const { modal } = this.state;
    const { leadData } = this.props;
    return (
      <div >
        <div className='campaign_navbar' >
          <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Leads</h1>
          <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i className="fa fa-question-circle-o" aria-hidden="true"></i></p>
        </div>
        <div>
          <Modal className="Leadcatcher_modal" isOpen={modal} toggle={this.toggle} className={LeadCatcher}>
            <ModalHeader className="Leadcatcher_modalheader" toggle={this.toggle}>email id</ModalHeader>
            <ModalBody className="Leadcatcher_modalbody" >
              <LeadCatchermodel />
            </ModalBody>
          </Modal>
        </div>
        <div className="graph_container" style={{ display: "flex", flexDirection: "row-reverse" }}>
          <span className="graph_title">Last 30 days</span>
        </div>
        <Container fluid>
          <Row>
            <Col md={3} className=''>
              <div className='grand_parent'>
                <div className='input_field'>
                  <Input type='email' className='in' placeholder='Search' />
                  <div className='child'>
                    <a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                      <span className='font_icon'><i className="fa fa-search" aria-hidden="true"></i></span>
                    </a>
                  </div>
                </div>
              </div>
            </Col>
            <Col md={3}>
              <div >
                <select className='filter_select1 w-100 mt-3' >
                  <option value='one'>All Campaigns</option>
                  <option value='two'>Campaign 1</option>
                  <option value='three'>Campaign 2</option>

                </select>
              </div>
            </Col>
            <Col md={3}>
              <div>
                <select className='filter_select1 mt-3'>
                  <option value='one'>unassigned</option>
                  <option value='two'>unassigned1</option>
                  <option value='three'>unassigned2</option>
                </select>
              </div>
            </Col>
            <Col md={2}>
              <div>
                <select className='filter_select1 mt-3'>
                  <option value='open'>open</option>
                  <option value='lost'>lost</option>
                  <option value='won'>won</option>
                  <option value='ignore'>ignore</option>
                </select>
              </div>
            </Col>
            <Col md={1}>
              <div className='refresh_child mt-3'>
                <a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                  <span className='font_icon'><i className="fa fa-undo" aria-hidden="true"></i></span>
                </a>
              </div>
            </Col>
          </Row>
          <Table className="align-items-center" responsive>
            <thead className="thead-light">
              <tr>
                <th scope="col"><input type="checkbox" /></th>
                <th scope="col">Person</th>
                <th scope="col">Campaign</th>
                <th scope="col">AssignedTo</th>
                <th scope="col">LeadDate</th>
              </tr>
            </thead>
            <tbody>
              {leadData && leadData.map((item, index) => {
                return (
                  <>
                    <tr key={index} className='pointer'>
                      <td className="check_box"><input type="checkbox" /></td>
                      <td onClick={this.toggle}>{item.email}</td>
                      <td onClick={this.toggle}></td>
                      <td onClick={this.toggle}></td>
                      <td onClick={this.toggle}></td>
                    </tr>
                  </>
                )
              })}
            </tbody>
          </Table>
        </Container>
        {/* <div className="Leadcatcher_table">
            <table >
              <thead>
                <tr>
                  <th ><input type="checkbox" /></th>
                  <th >Person</th>
                  <th >Campaign</th>
                  <th >AssignedTo</th>
                  <th >LeadDate</th>
                </tr>
              </thead>
              <tbody>
                {
                  leadData && leadData.map((item, index) => {
                    <tr key={index}>
                      <td className="check_box"><input type="checkbox" /></td>
                    </tr>
                  })
                }
                <tr onClick={this.toggle}>
                  <td className="check_box"><input type="checkbox" /></td>
                  <td className="Campaign_title">Person name</td>
                  <td className="Created">Campaign name</td>
                  <td className="Assigned">Omaid Faizyar</td>
                  <td className="Recipient">00:00</td>
                </tr>
              </tbody>
            </table> */}
      </div >
    )
  }
}
const mapStateToProps = (state) => {
  console.log("state", state.LeadViewReducer && state.LeadViewReducer.leadViewData)
  return {
    leadData: state.LeadViewReducer && state.LeadViewReducer.leadViewData
  };
};
const mapDispatchToProps = (dispatch) => ({
  // CampaignLeadGetAction:()=>dispatch(CampaignLeadGetAction)
  CampaignLeadViewAction: () => dispatch(CampaignLeadViewAction())

});
export default connect(mapStateToProps, mapDispatchToProps)(LeadCatcher)
