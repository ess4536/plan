import React from 'react';
import {Switch,Route,} from 'react-router-dom'; 
import PlanList from './PlanList';
import NewPlan from './NewPlan';
import './Main.css';

class Main extends React.Component {
  
  render() {
    return (
      <div className='main'>
        <Switch>
          <Route exact path='/' component={PlanList} />
          <Route path='/new-plan' component={NewPlan} />
        </Switch>
      </div>
    );
  }
}

export default Main;
