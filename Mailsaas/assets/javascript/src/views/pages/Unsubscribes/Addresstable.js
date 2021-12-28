import React from 'react'
import { Container, Row, Col, Table } from 'reactstrap'

function Addresstable(props) {
    return (
        <div>
            <Container fluid >
                <Row>
                    <Table responsive hover>
                        <thead>
                            <tr>
                                <th>
                                    {/* <input ref={props.textInput} onChange={props.selectAll} style={{width:'20px',height:'20px'}} type="checkbox" /> */}
                                </th>
                                <th className="Email">Email</th>
                                <th className="name">Name</th>
                                <th className="IsAdmin">UNSUBSCRIBE DATE</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                props.data.map((e,i)=><tr key={i} className='' >
                                    <td ><input name={i} onChange={(event)=>{props.showSelectionBar(e.id,event)}} style={{width:'20px',height:'20px'}}  type="checkbox" /></td>
                                    <td className="name-value">{e.email} </td>
                                    <td className="Email-value">{e.name}</td>
                                    <td className="IsAdmin-value">{e.date.substring(0,10)}</td>
                                </tr>
                                )
                            }
                           
                        </tbody>
                    </Table>
                </Row>
            </Container>

        </div>
    )
}

export default Addresstable
