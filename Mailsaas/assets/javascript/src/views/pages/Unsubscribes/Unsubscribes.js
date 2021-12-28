import React from 'react'
import { TabContent, TabPane, NavLink, Nav, NavItem } from 'reactstrap'
import { Container, Row } from 'reactstrap'
import Domainpage from './Domainpage'
import Addresstable from "./Addresstable"
import classnames from 'classnames';
import { fetchUnsubscribeAction, deleteUnsubscribeUsersAction, unsubscribeUsersWithCsvAction, unsubscribeUsersWithEmailAction, requestUserUnsubscribeWithCsv, } from '../../../redux/action/UnsubscribeActions'
import { Component } from 'react';
import { connect } from "react-redux";
import UnsubscribesModal from './UnsubscribesModal'
import '../../../../../scss/custom/custom.scss'
const SpanStyles = {
  paddingRight: "10px",
  paddingLeft: "10px",
  color: "white",
  fontSize: "25px",
  cursor: 'pointer'
};
const Span = {
  paddingRight: "20px",
  paddingLeft: "20px",
  color: "white",
  fontSize: "25px",
  borderRight: "1px dashed",
  marginRight: "10px"
};
class Unsubscribes extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeTab: '1',
      selectedId: [],
      checked: false,
      isSelectionBar: false,
      modal: false,
      email: '',
    }
  }
  handleClose = () => {
    this.setState({
      modal: false
    })
  }
  toggle = tab => {
    if (this.state.activeTab !== tab)
      this.setState({ activeTab: tab })
  }
  componentDidMount() {
    this.props.fetchUnsbcribed()
  }
  showSelectionBar = (id, e) => {
    console.log(e.target.name, "h")
    const { selectedId } = this.state
    this.setState({
      isSelectionBar: true,
      currentChecked: e.target.name
    })
    if (selectedId.length === 0) {
      selectedId.push(id)
      return
    }
    for (let index = 0; index < selectedId.length; index++) {
      if (id === selectedId[index]) {
        let array = selectedId.filter(e => e != id)
        this.setState({
          selectedId: array
        }, () => { console.log(array, "select") })
        return
      }
    }
    selectedId.push(id)
    console.log(selectedId, "sdfsdg")
  }
  UnsubscribeDelete = () => {  
    let data = this.state.selectedId;
    this.props.deleteUnsubscribeUsers(data)
    this.setState({
      isSelectionBar: false,
      checked: false,
      selectedId:[]
    },()=>{})

  }
  selectAll = (e) => {
    this.setState({
      checked: e.target.checked
    })
    console.log(this.textInput.current.checked, " this.textInput.current.checked")
  }
  unsubscribeWithEmail = (e) => {
    console.log(e.target.value)
    this.setState({
      email: e.target.value
    })
  }
  unsubscribeWithCsv = (e) => {
    let fileData = new FormData();
    fileData.append('csv_file', e.target.files[0])
    if (e.target.files[0]) {
      this.props.unsubscribeUsersWithCsvAction(fileData)
    }
    this.setState({
      modal: false
    })
  }
  handleSubmit = () => {
    this.setState({ modal: false })
    this.props.unsubscribeUsersWithEmailAction(this.state.email)
  }
  render() {
    const { isSelectionBar, selectedId, checked, currentChecked } = this.state;
    return (
      <div>
        <div>
          <div className='campaign_navbar' >
            <p style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Unsubscribes</p>
            <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i className="fa fa-question-circle-o" aria-hidden="true"></i></p>
          </div>
          <div style={{ padding: '20px' }} className={`selection-bar ${isSelectionBar && selectedId.length > 0 ? "_block" : " "}`} >
            <span style={SpanStyles} onClick={() => { this.setState({ isSelectionBar: false }); selectedId.length = 0 }}><i className="fa fa-close" aria-hidden="true"></i></span>
            <span style={Span} >{selectedId.length} selected</span>
            <div onClick={this.UnsubscribeDelete}>
              <span style={SpanStyles}><i className="fas fa-minus-circle"></i></span>
              <span style={SpanStyles} >Delete</span>
            </div>
          </div>
        </div>
        <Container fluid>
          <Row className="mt-3 ml-1">
            <div>
              <input className="searchbox-unsubscribe" type="search" placeholder="search"></input>
            </div>
            <div className="unsubscribe-buttonsdiv">
              <div>
                <button className="refresh-button" ><i style={{ fontSize: "15px" }} className="fa fa-refresh" aria-hidden="true"></i>
                  <span onClick={() => window.location.reload()} style={{ marginLeft: "10px" }}>REFRESH</span></button></div>
              <div><button className="Export-button">EXPORT</button></div>
            </div>
          </Row>
          <Row className="mt-5 ml-1">
            <Nav tabs style={{ borderBottom: "1px solid #ccc", width: "99%" }} >
              <NavItem className="address-nav"><NavLink className={classnames({ active1: this.state.activeTab === '1' })} onClick={() => { this.toggle('1'); }}><span style={{ color: 'black' }}>ADDRESS</span></NavLink></NavItem>
              <NavItem className="domain-nav"><NavLink className={classnames({ active2: this.state.activeTab === '2' })} onClick={() => { this.toggle('2'); }}><span style={{ color: 'black' }}>DOMAIN</span></NavLink></NavItem>
            </Nav>
          </Row>
          <Row>
            <TabContent activeTab={this.state.activeTab} style={{ width: "100%" }}>
              <TabPane tabId="1">
                <Addresstable
                  currentChecked={currentChecked}
                  selectAll={this.selectAll}
                  checked={checked}
                  showSelectionBar={this.showSelectionBar}
                  data={this.props.data}
                  textInput={this.textInput}
                />
              </TabPane>
              <TabPane tabId="2">
                <Domainpage />
              </TabPane>
            </TabContent>
          </Row>
        </Container>
        <div className='plus-button-div' onClick={(e) => { e.preventDefault(), this.setState({ modal: !this.state.modal }) }}>
          <div className='new_add_button'>
            <span className="plusicon" >+</span>
          </div>
        </div>
        <UnsubscribesModal
          isOpen={this.state.modal}
          handleSubmit={this.handleSubmit}
          handleClose={this.handleClose}
          unsubscribeWithEmail={this.unsubscribeWithEmail}
          unsubscribeWithCsv={this.unsubscribeWithCsv}
          handleSubmit={this.handleSubmit}
          loading={this.props.loading}
        />

      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.UnsubscribeReducer.unsubscribeData,
    loading: state.UnsubscribeReducer.loading
  };
};
const mapDispatchToProps = dispatch => ({
  fetchUnsbcribed: () => { dispatch(fetchUnsubscribeAction()) },
  deleteUnsubscribeUsers: (data) => { dispatch(deleteUnsubscribeUsersAction(data)) },
  unsubscribeUsersWithCsvAction: (data) => { dispatch(unsubscribeUsersWithCsvAction(data)) },
  unsubscribeUsersWithEmailAction: (data) => { dispatch(unsubscribeUsersWithEmailAction(data)) }
});
export default connect(mapStateToProps, mapDispatchToProps)(Unsubscribes);