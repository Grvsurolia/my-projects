import React, { Component } from 'react'
import { Form, Button, Modal } from 'react-bootstrap';
import axios from 'axios';
import { API_URL } from '../Constants';


export default class Emails extends Component {
    constructor() {
        super()
        this.state = {
            show: false,
            subject: '',
            csvFile: '',
            body: '',
            emails: [],
        }
    }
    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    handleCsvChange = (e) => {
        this.setState({
            csvFile: e.target.files[0],
        });
    }
    handleSubmit = (e) => {
        e.preventDefault();
        this.setState({
            show: false,
        })

        console.log(this.state)
        console.log(this.state.csvFile, "csv")
        const formData = new FormData();
        formData.append('csvfile', this.state.csvFile);
        formData.append('subject', this.state.subject);
        formData.append('email_body', this.state.body);
        axios({
            method: 'POST',
            url: `${API_URL}/mail/email/`,
            data: formData,
        })
            .then((response) => {
                console.log(response)
                this.getApi();
            })
            .catch(error => {
                console.error('There was an error!', error);
            })
    }
    getApi = () => {
        axios.get(`${API_URL}/mail/email/`)
            .then((response) => {
                return (this.setState({ emails: response.data.data }))
            })
            .catch(error => {
                console.error('There was an error!', error);
            })
    }
    componentDidMount() {
        this.interval = setInterval(() => {
            this.getApi();
        }, 30000);
        this.getApi();
    }
    render() {
        const { show, emails } = this.state;
        return (
            <div className='main-email-div'>
                <h3>List of Emails</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Email Sender</th>
                            <th>Email Receiver</th>
                            <th>Status</th>
                            <th>CSV Name</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            emails.map((value, index) => {
                                return (<tr key={index}>
                                            <td>{index + 1}</td>
                                            <td>{value.sender}</td>
                                            <td>{value.receiver}</td>
                                            <td>{value.status ? 'Sent' : 'Bounced'}</td>
                                            <td>{value.csv_name}</td>
                                </tr>)
                            })
                        }
                    </tbody>
                </table>
                <Modal show={show} backdrop="static" keyboard={false}>
                    <Form onSubmit={this.handleSubmit}>
                        <Modal.Header ><Modal.Title>Emails <span className='float-right' onClick={() => { this.setState({ show: false }) }} >&#10006;</span></Modal.Title></Modal.Header>
                        <Modal.Body>
                            <label>Upload Csv file</label>
                            <input type='file' accept=".csv" className='form-control' name='csvFile' onChange={this.handleCsvChange} required></input>
                            <label>Subject</label>
                            <input type='text' className='form-control' name='subject' value={this.state.subject} onChange={this.handleChange} required></input>
                            <label>Email Body</label>
                            <textarea type='text' className='form-control' name='body' value={this.state.body} onChange={this.handleChange} required></textarea>

                        </Modal.Body>
                        <Modal.Footer>
                            <Button variant="secondary" onClick={() => { this.setState({ show: false }) }} >Close</Button>
                            <Button variant="primary" type='submit'> Add</Button>
                        </Modal.Footer>
                    </Form>
                </Modal>
                <Button className='add' onClick={() => { this.setState({ show: true }) }}>Email</Button>
            </div>
        )
    }
}
