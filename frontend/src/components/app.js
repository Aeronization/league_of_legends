import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from  "./layout/Header"
import Champion from  "./champions/Champion"

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <Champion />
            </Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));