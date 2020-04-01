import React from 'react';
import axios from 'axios';
import Like from './Like';
import './TaskList.css';

class PlanList extends React.Component {
  constructor(props){
    super(props);
    this.state={
      planList: [],
      taskList: [],
      isLoaded: false,
    }
  }

  componentDidMount(){
    try{
      axios.get('http://localhost:8000/api/v1/plan')
        .then((response) => {
          this.setState({
            planList: response.data.results,
          });
          console.log(this.state.planList);
        });
      axios.get('http://localhost:8000/api/v1/task')
        .then((response) => {
          this.setState({
            taskList: response.data.results,
            isLoaded: true,
          });
          console.log(this.state.taskList);
        });
    }catch(e){
      console.log(e)
    }
  }
  
  render() {
    if(!this.state.isLoaded){
      return(
        <p>Loding...</p>
      )
    }else{
      const planList = this.state.planList;
      const taskList = this.state.taskList;
      console.log(planList);
      console.log(taskList);
      return (
        <div className='plan-list'>
          {
            this.state.planList.map((plan, index) => {
              return (
                  <div key={index}>
                    <div className= "task">
                      <div className="content">
                        <div className="task-name">
                          <p>{plan.plan_name}</p>
                        </div>
                        <div className="task-place">
                          <img src="../../images/place.jpg" alt="" className="map-icon"/>
                          <p>愛知県/名古屋市</p>   
                        </div>

                        <div className="task-img">
                          <img src="../../images/turumai.jpg" alt="" />
                        </div>
                        <Like />

                        <div className="task-url">
                          <p></p>
                        </div>

                        {(() => {
                          const items = [];
                          for (let i=0; i<taskList.length; i++) {
                            if(taskList[i].plan === plan.id){
                              items.push(<p>{taskList[i].task_name}</p>)
                            }
                          }
                          return <div className="task-memo">{items}</div>;
                        })()}
                      </div>
                    </div>
                  </div>
              )
            })
          }
        </div>
      );
    }
  }
}

export default PlanList;