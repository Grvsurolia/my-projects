import React from 'react';
import { TabContent, Container, TabPane, Nav, NavItem, Row, Col } from 'reactstrap';
import { Link, Route } from 'react-router-dom';
import NewCampaign_start from "../../pages/dashboards/NewCampaign_start";
class NewCampaign extends React.Component {
    render() {
        return (
            <>
                <Container fluid>
                    <Row style={{ width: '100%', borderBottom: "1px solid #dedede" }}>
                        <Col md={2} style={{ display: 'flex', alignItems: 'center' }}>
                            <div className='logo_div' style={{ display: 'flex', alignItems: 'center' }}>
                                <div><img src={STATIC_FILES.mailsaas_logo_32}></img>
                                    <span style={{ color: 'black', fontSize: '20px' }}>MailSaaaS</span></div>
                            </div>
                        </Col>
                        <Col md={8}>
                            <h1 style={{ textAlign: 'center', fontSize: '6em', color: "#333333" }}>New Campaign</h1>
                        </Col>
                        <Col md={2} style={{ display: "flex", flexDirection: "row-reverse" }}>
                            <div className='mt-3'>
                                <a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                    <span><i className="fa fa-question-circle-o fa-lg" aria-hidden="true"></i></span>
                                </a>
                            </div>
                        </Col>
                    </Row>
                    <Row>
                        <hr color='yellow'></hr>
                    </Row>
                    <Row className='mx-auto '>
                        <ul style={{ listStyleType: 'none', display: 'flex' }}>
                            <li className='mr-3 ml-3'><Link to="/app/admin/CampaignStart">START</Link></li>
                            <li className='mr-3 ml-3'><Link to="/app/admin/CampaignRecipient">RECIPICIENT</Link></li>
                            <li className='mr-3 ml-3'><Link to="/app/admin/CampaignCompose">COMPOSE</Link></li>
                            <li className='mr-3 ml-3'><Link to="/app/admin/CampaignPreview">PREVIEW</Link></li>
                            <li className='mr-3 ml-3'><Link to="/app/admin/CampaignOptions">OPTIONS</Link></li>
                            <li className='mr-3 ml-3'><Link to="/app/admin/CampaignSend">SEND</Link></li>
                        </ul>
                    </Row>
                </Container>

            </>
        );
    }
}
export default NewCampaign;
