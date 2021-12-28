/*!

=========================================================
* Argon Dashboard PRO React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-pro-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
/home/hr-01/project/MailSaaS/assets/javascript/src/components/Navbars/AdminNavbar.js
*/
import React from "react";
import classnames from "classnames";
import AdminNavbar from '../../../../../javascript/src/components/Navbars/AdminNavbar'
// node.js library that concatenates classes (strings)
import CardHeader from "../../../../src/components/Headers/CardsHeader"
// importing routing module
import { Link } from 'react-router-dom'
import SimpleHeader from "../../../components/Headers/SimpleHeader.js";
import {
  Button,
  Container,
  Row,
  Col,
  Card,
  CardHeader as ReactstrapCardHeader,
  CardTitle,
  CardText,
  CardBody,
  Nav,
  Navbar
} 
from "reactstrap";
// /home/hr-01/project/MailSaaS/assets/javascript/src/components/Headers/CardsHeader.js
class Dashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activeNav: 1,
      chartExample1Data: "data1"
    };
  }
  toggleNavs = (e, index) => {
    e.preventDefault();
    this.setState({
      activeNav: index,
      chartExample1Data:
        this.state.chartExample1Data === "data1" ? "data2" : "data1"
    });
  };
  render() {
    return (
      <div>
          <SimpleHeader name="Buttons" parentName="Components" />
          <Container className="mt--6" fluid>
            <Row className="justify-content-center">
              <Col className="card-wrapper" lg="8">
                <Card>
                  <ReactstrapCardHeader>
                    <h3 className="heading-title text-info mb-0 text-center">
                      Welcome to MailSaaS
                    </h3>
                  </ReactstrapCardHeader>
                  <CardBody>
                    <CardTitle className="mb-3" tag="h3">
                      Create Capmaing
                    </CardTitle>
                    <CardText className="mb-4">
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                      A simple solution for email outreach.
                    </CardText>
                    <Link to="/app/admin/CampaignStart">
                      <Button className="btn-icon" color="primary" type="button">
                        <span className="btn-inner--icon mr-1">
                          <i className="ni ni-fat-add" />
                        </span>
                        <span className="btn-inner--text">NEW CAMPAIGN</span>
                      </Button>
                    </Link>
                  </CardBody>
                </Card>
              </Col>
            </Row>
          </Container>
        {/* <AdminNavbar />
        <CardHeader /> */}
      </div>
    );
  }
}

export default Dashboard;