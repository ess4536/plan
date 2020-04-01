import React from 'react';
import {withRouter, Link} from 'react-router-dom';
import './Footer.css';

class Footer extends React.Component {
  handleClick(){
    this.props.history.push('/new-plan');
  }

  render() {
    return (
      <div className='footer'>
        <input type="image" src="../../images/new.png" alt="" onClick={()=>{this.handleClick()}}/>
      </div>
    );
  }
}

export default withRouter(Footer);
