import React, { Component } from 'react'
import { connect } from 'react-redux';
import { Container, Row, Col, Label, Input, Table, Dropdown, DropdownToggle, DropdownMenu, DropdownItem } from 'reactstrap'
import { OnclickProspectActionData } from '../../../redux/action/ProspectsAction'
export class ProspectOnclick extends Component {
    constructor(props){
        super(props)
    }
    componentDidMount() {
        this.props.OnclickProspectActionData(this.props.id);
    }
    render() {
        const { propData } = this.props;
        return (
            <div>
                <Container fluid className='mt-4'>
                    <Row>
                        <Table responsive hover className='prospect_table'>
                            <thead >
                                <tr>
                                    {/* <th><input type='checkbox' /></th> */}
                                    <th >campaign</th>
                                    <th>ADDED</th>
                                    <th>STATUS</th>
                                    <th>SENT</th>                                   
                                    <th>REPLIES</th>
                                    <th>OPEN</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    {/* <td ><input type='checkbox' /></td> */}
                                    <td>{propData && propData.campaign_title}</td> 
                                    <td>{propData && propData.added}</td>
                                    <td>{propData && propData.lead_status}</td>
                                    <td>{propData && propData.sent_in_a_camp}</td>
                                    <td>{propData && propData.replies}</td>    
                                    <td>{propData && propData.opens}</td>                                   {
                                    }
                                    
                                </tr>
                            </tbody>

                        </Table>
                    </Row>
                </Container>

            </div>
        )
    }
}

const mapStateToProps = (state) => {
    console.log("cheking state for onclick",state.OnclickProspectsReducer.prospectOnclickData &&state.OnclickProspectsReducer.prospectOnclickData.campaign_title)
    return {
        propData: state.OnclickProspectsReducer.prospectOnclickData &&state.OnclickProspectsReducer.prospectOnclickData
        // id:state.ProspectsGetReducer
        // id:state.OnclickProspectsReducer.prospectOnclickData && state.OnclickProspectsReducer.prospectOnclickData.id
    }
}
const mapDispatchToProps = dispatch => ({
    OnclickProspectActionData: prospectOnclickData => { dispatch(OnclickProspectActionData(prospectOnclickData)) }
})
export default connect(mapStateToProps, mapDispatchToProps)(ProspectOnclick)