import React, { Component } from 'react'
import {
  Card,
  Input,
  Table,
  Container,
  Row,
  Col,
  Modal,
  Button
} from "reactstrap";
import { Link } from 'react-router-dom';
import { connect } from "react-redux";
// import SMTP from "../../../../src/views/pages/MailAccount/SMTP"
import { CampaignTableAction, CampaignSaveAction, CampaignOverviewAction } from '../../../redux/action/CampaignAction'
import SearchNavbar from '../../../components/Navbars/SearchNavbar';
class Campaign extends Component {
  constructor(props) {
    super(props)
    this.state = {
      show: true,
      hide: true,
      data: [],
      checked: false,
      exampleModal: false
    }
  }
  componentDidMount() {
    const CampId = this.props.history.location.state && this.props.history.location.state
    console.log("campID", CampId)
    this.props.CampaignTableAction()
  }
  allCheck = (e) => {
    const table = this.props.Tables.CampaignTableData
    for (let i = 0; i < table.length; i++) {
      this.setState({
        checked: !this.state.checked,
        exampleModal: !this.state.exampleModal
      })
    }
  }
    singleCheck(index){
      let tables=this.props.Tables.CampaignTableData.slice();
      tables[index].checked=!tables[index].checked
      this.setState({
        checked:tables
      })
    }
    // handleCheck = (e) => {
    //   let tables = this.props.Tables.CampaignTableData
    //   tables.forEach(table => {
    //     if (table.value === e.target.value)
    //       table.isChecked = e.target.checked
    //   })
    //   this.setState({ tables: tables })
    // }
    // toggleModal = ()=> {
    //   this.setState({
    //     exampleModal: !this.state.exampleModal
    //   });
    // };
  
  render() {
    const { show, hide, checked, exampleModal } = this.state;
    const { Tables, CampaignOverviewAction } = this.props;

    return (
      <>
      <SearchNavbar />
        <div className='main-view'>
          {/* <div className='campaign_navbar' >
            <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Campaigns</h1>
            <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i className="fa fa-question-circle-o" aria-hidden="true"></i></p>
          </div> */}
          <Container fluid className=''>
            <Row>
              {/* <Col md={2} className='mt-1'>
                <div className='grand_parent' >
                  <div className='input_field'>
                    <Input type='email' className='in' placeholder='Search' />
                    <div className='child mt-2'>
                      <a href='#'> <span className='font_icon'><i className="fa fa-search" aria-hidden="true"></i></span></a></div>
                  </div>
                </div>
              </Col> */}
              <Col md={1}>
                <div>
                  <label className='filter_app'>Teammate</label><br></br>
                  <select className='filter_select'>
                    <option value='Any'>Any</option>
                    <option value='Unassigned'>Unassigned</option>
                    <option value='name'>Name</option>
                  </select>
                </div>
              </Col>
              <Col md={9}></Col>
            </Row>
            <Row className='mt-4'>
              {show && <Col md={1} style={{ height: '40px' }}>
                <div className='campaign_label'>
                  <div className='add_label' onClick={(e) => { e.preventDefault(), this.setState({ show: !show }) }}> <span>+ Label</span></div>
                </div>
              </Col>}
              {!show && <Col md={3}>
                <div className='grand_parent' >
                  <div className='input_field'>
                    <Input type='email' className='label_input w-100' placeholder='Create a campaign label' />
                    <div className='child mt-2'>
                      <a href='' onClick={(e) => { e.preventDefault(), this.setState({ show: true }) }}>
                        <span className='font_icon'><i className="fa fa-check" aria-hidden="true"></i></span>
                      </a>
                    </div>
                    <div className='child mt-2'>
                      <a href='' onClick={(e) => { e.preventDefault(), this.setState({ show: true }) }}>
                        <span className='font_icon'><i className="fa fa-check" aria-hidden="true"></i></span>
                      </a>
                    </div>
                  </div>
                </div>
              </Col>}
              <Col md={1}>
                <div className='campaign_label'>
                  <div className='add_label'> <span>
                    <i className="fa fa-ban" aria-hidden="true"></i><span style={{ fontSize: '1em' }}>Unlabeled</span></span></div>
                </div>
              </Col>
              <Col md={1}>
                <div className='campaign_label'>
                  <div className='add_label' onMouseOut={(e) => { e.preventDefault(), this.setState({ hide: hide }) }} onMouseMove={(e) => { e.preventDefault(), this.setState({ hide: !hide }) }}>
                    <span><i className="fa fa-tags" aria-hidden="true"></i>testlabel<span>
                    </span>
                    </span>
                  </div>
                </div>
              </Col>
            </Row>
          </Container>
          <Container fluid className='mt-4' >
            <Card>
              <Row>
                <Col md={12}>
                  <Table responsive hover style={{ textAlign: 'center' }}>
                    <thead>
                      <tr>
                        <th scope="col" className="tableheader1" >
                          <input type="checkbox" checked={this.state.checked} onClick={(e) => { (this.allCheck(e)) }} /></th>
                        <th></th>
                        <th className="tableheader2">Campaign Title</th>
                        <th className="header_created">Created</th>
                        <th className="header_assigned">Assigned</th>
                        <th className="header_recipents">RECIPIENTS</th>
                        <th className="header_sent">SENT</th>
                        <th className="header_leads">LEADS</th>
                        {/* <th className="header_replies">REPLIES</th> */}
                        <th className="header_open">OPENS</th>
                        {/* <th className="header_bounces">BOUNCES</th> */}
                      </tr>
                    </thead>
                    <tbody>
                      {Tables && Tables.CampaignTableData.map((item, index) => {
                        return (<>
                          <tr key={index} className='pointer' >
                            <td><input type='checkbox' onChange={(index) => this.singleCheck(index)} checked={this.state.checked} /></td>
                            <td><i class="fas fa-pause"></i></td>
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className="Campaign_title">{item.camp_title}</td>
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Created'>{item.camp_created_date_time.slice(0, 3).concat(item.camp_created_date_time.slice(-3,))}</td>
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Assigned'>{item.assigned}</td>
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Recipient'>{item.recipientCount}</td>
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Sent'>{item.sentCount}</td>
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Leads'>{item.leadCount}</td>
                            {/* <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Replies'>-</td> */}
                            <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} className='Open'>{item.opensCount}</td>
                            {/* <td onClick={() => { this.props.CampaignOverviewAction(item.id) }} key={index} className='Bounces'>-</td> */}
                          </tr>
                        </>
                        )
                      })}
                    </tbody>
                    <Modal
                      className="modal-dialog-centered" isOpen={this.state.exampleModal} >
                      <div className="modal-header">
                        <h5 className="modal-title" id="exampleModalLabel">Modal title</h5>
                        <button aria-label="Close" className="close" data-dismiss="modal" type="button" onClick={() => this.setState({ exampleModal: !exampleModal, checked: !checked })} >
                          <span aria-hidden={true}>×</span>
                        </button>
                      </div>
                      <div className="modal-body">...</div>
                      <div className="modal-footer"><Button color="secondary" data-dismiss="modal" type="button" onClick={() => this.setState({ exampleModal: !exampleModal, checked: !checked })}> Close </Button>
                        <Button color="primary" type="button"> Save </Button>
                      </div>
                    </Modal>

                  </Table>
                </Col>
              </Row>
            </Card>
          </Container>
          <div className='plus-button-div' style={{ position: 'fixed', bottom: 0, right: 5 }}>
            <div className='new_add_button' >
              <Link to="/app/admin/CampaignStart"> <span className="plusicon">+</span></Link>
            </div>
          </div>
        </div>
      </>
    )
  }
}
const mapStateToProps = (state) => {
  return {
    Tables: state.CampaignTableReducer
  };
};
const mapDispatchToProps = dispatch => ({
  CampaignTableAction: mailGetData => { dispatch(CampaignTableAction(mailGetData)); },
  CampaignSaveAction: saveData => { dispatch(CampaignSaveAction(saveData)) },
  CampaignOverviewAction: id => { dispatch(CampaignOverviewAction(id)) }
});
export default connect(mapStateToProps, mapDispatchToProps)(Campaign)
