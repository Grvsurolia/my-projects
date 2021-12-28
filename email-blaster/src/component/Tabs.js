import React, { Component } from 'react'
import SMTP from "../component/SMTP"
import Emails from "../component/Emails"
import { Tabs, Tab } from 'react-bootstrap';


export default class EmailTabs extends Component {
    render() {
        return (
            <>
                <div className='tabs-div'>
                    <Tabs defaultActiveKey="smtp" id="uncontrolled-tab-example">
                        <Tab eventKey="smtp" title="SMTP" >
                            <SMTP />
                        </Tab>
                        <Tab eventKey="emails" title="Emails">
                            <Emails />
                        </Tab>

                    </Tabs>
                </div>
            </>
        )
    }
}
