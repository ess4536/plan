import React from 'react';
import axios from 'axios';
import './NewPlan.css';

class NewPlan extends React.Component {
  constructor(props){
    super(props);
    this.state={
      isLoaded: false,
      plan_name: "",
      tasks: [
        {
          task_name: "",
          image_src: "",
          start_datetime: "",
          end_datetime: "",
          url: "",
          task_memo: "",
          plan: -1,
        }
      ],
    };
  }
  
  handleChange(e, index){
    if(["task_name", "image_src", "start_datetime", "end_datetime", "url", "task_memo", "plan"].includes(e.target.name)){
      this.state.tasks[index][e.target.name] = e.target.value;
      if(e.target.name === "image_src"){
        var createObjectURL = (window.URL || window.webkitURL).createObjectURL || window.createObjectURL;
        var files = e.target.files;
        var image_url = files.length===0 ? "" : createObjectURL(files[0]);
        this.state.tasks[index][e.target.name] = image_url;
      }
      this.setState({tasks: this.state.tasks});
      console.log(index);
      console.log(this.state.tasks);
    }else{
      this.setState({[e.target.name]: e.target.value});
    }
  }

  addTask(){
    this.setState({tasks: [...this.state.tasks, {task_name: "", start_datetime: "", end_datetime: "", url: "", task_memo: "", plan: -1,}]});
  }

  handleSubmit(e){
    try{
    // axios.post(
    //   'http://localhost:8000/api/v1/plan/', 
    //   {
    //     plan_name: this.state.plan_name
    //   }
    // ).then((response) => {
    //     console.log(response);
    //   });
    }catch(e){
      console.log(e);
    }
      
    try{
    axios.get(
      'http://localhost:8000/api/v1/plan/'
    ).then((response) => {
        let count = response.data.count;
        let latest_data = response.data.results[count-1];
        console.log(latest_data);
        let plan_id = latest_data.id;
        this.setState({
          isLoaded: true,
        });
        
        for(var i=0; i<this.state.tasks.length; i++){
          this.state.tasks[i]["plan"] = plan_id;
          this.setState({tasks: this.state.tasks});
          console.log(this.state.tasks[i])
          // axios.post(
          //   'http://localhost:8000/api/v1/task/', this.state.tasks[i]
          //   ).then((response) => {
          //     console.log(response);
          // });
        }
      });
    }catch(e){
      console.log(e);
    }
  }
  
  render() {
    return (
      <div className='post'>
        <form>
          <div className="plan-name">
            <input type="text" name="plan_name" value={this.state.plan_name} onChange={(e) => {this.handleChange(e, 0)}}/>
          </div>
          <div className = "task">
            <div className="content">
            {
              this.state.tasks.map((task, index) => {
                return (
                  <div key={index}>
                    <div className="task-name">
                      <label>タイトル</label>
                      <input type="text" name="task_name" value={task.task_name} onChange={(e) => {this.handleChange(e, index)}}/>
                    </div>

                    <label>開始</label>
                    <input type="datetime-local" name="start_datetime" value={task.start_datetime} onChange={(e) => {this.handleChange(e, index)}}/>
                    
                    <label><br/>終了</label>
                    <input type="datetime-local" name="end_datetime" value={task.end_datetime} onChange={(e) => {this.handleChange(e, index)}}/>
                    
                    <div className="task-img">
                    <label className="Addimg">
                      <input type="file" class="add_input" name="image_src" accept="image/*" capture="camera" onChange={(e) => {this.handleChange(e, index)}}/>
                      <img src={task.image_src} />
                    </label>
                    </div>

                    <div className="task-url">
                      <label>参考URL</label>
                      <input type="url" name="url" value={task.url} onChange={(e) => {this.handleChange(e, index)}}/>
                    </div>

                    <div className="task-memo">
                      <label>内容</label>
                      <input type="text" name="task_memo" value={task.task_memo} onChange={(e) => {this.handleChange(e, index)}}/>
                    </div>
                  </div>
                )
              })
            }
            <button type="button" className="btn-square" onClick={() => this.addTask()}>+</button>
          </div>
        </div>
        </form>
          <button className="btn-square btn-submit" onClick={() => this.handleSubmit()}>登録</button>
      </div>
    );
  }
}

export default NewPlan;