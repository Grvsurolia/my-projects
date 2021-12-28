import React, { Component } from 'react'
import { Container, Row, Col, Card } from 'reactstrap'
export class AppsandCrm extends Component {
    render() {
        return (
            <div className='main-view'>
                <div className='campaign_navbar' >
                    <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Apps & CRMs</h1>
                    <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i className="fa fa-question-circle-o" aria-hidden="true"></i></p>
                </div>
                <div className='Apps'>
                    <h1 className='N-I display-4'style={{borderBottom:"1px solid #ccc",paddingBottom:"10px"}} >NATIVE INTEGRATIONS</h1>
                    {/* <hr color='silver'></hr> */}
                    <div className='native_media'>
                        <Container  fluid>
                            <Row className="mt-5">
                                <Col md={3}>
                                    <a href="" className='native_link'>
                                        <div className='native_media_div'>
                                            <div>
                                                <img alt="..." src={STATIC_FILES.sales_force} className='native_img'></img>
                                            </div>
                                            <div>
                                                <span><b>SALESFORCE</b></span>
                                                <p>Track activities and update lead statuses when actions are taken in Mailshake.</p>
                                                <div className='native_add mx-auto'><a href=''>ADD</a></div>
                                            </div>
                                        </div>
                                    </a>
                                </Col>
                                <Col md={3}>
                                    <a href="" className='native_link'>
                                        <div className='native_media_div'>
                                            <div>
                                                <img alt="..." src={STATIC_FILES.slack} className='native_img'></img>
                                            </div>
                                            <div>
                                                <span><b>SLACK</b></span>
                                                <p>Post messages to your channels when you receive a new reply or lead.</p>
                                                <div className='native_add mx-auto'><a href=''>ADD</a></div>
                                            </div>
                                        </div>
                                    </a>
                                </Col>
                                <Col md={3}>
                                    <a href="" className='native_link'>
                                        <div className='native_media_div'>
                                            <div>
                                                <img alt="..." src={STATIC_FILES.pipe_drive} className='native_img'></img>
                                            </div>
                                            <div>
                                                <span><b>PIPEDRIVE</b></span>
                                                <p>Move deals through your stages, track activities, and update lead statuses.</p>
                                                <div className='native_add mx-auto'><a href=''>ADD</a></div>
                                            </div>
                                        </div>
                                    </a>
                                </Col>
                                {/* <Col md={3}>
                                    <a href="" className='native_link'>
                                        <div className='native_media_div'>
                                            <div>
                                                <img alt="..." src={STATIC_FILES.hub_spot} className='native_img'></img>
                                            </div>
                                            <div>
                                                <span><b>PIPEDRIVE</b></span>
                                                <p>Track activities, move deals through stages, and update contact statuses.</p>
                                                <div className='native_add mx-auto'><a href=''>ADD</a></div>
                                            </div>
                                        </div>
                                    </a>
                                </Col> */}
                            </Row>
                        </Container>
                    </div>
                    {/* <div>
                        <h1 className='N-I display-4 mt-5' style={{borderBottom:"1px solid #ccc",paddingBottom:"10px"}}>OTHER APPS AND CRMS</h1>
                       
                        <p>Through the power of <a href=''><b>Zapier</b></a>, you can connect Mailshake to all sorts of apps:</p>
                    </div> */}
                    {/* <div>
                        <label className='filter_app'>Filter by app</label><br></br>
                        <select className='filter_select'>
                            <option value='one'>One</option>
                            <option value='two'>two</option>
                            <option value='three'>three</option>
                            <option value='four'>Four</option>
                        </select>
                    </div> */}
                    {/* <div>
                        <Container>
                            <Row>
                                <Col>
                                    <Card>
                                    </Card>
                                </Col>
                            </Row>
                        </Container>
                    </div> */}
                </div>
            </div>
        )
    }
}
export default AppsandCrm