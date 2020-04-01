import React, { useState } from 'react';
import './PlanList.css';

function Like(props) {
  const [liked, setLike] = React.useState(false);
  const toggleLike = React.useCallback(() => setLike((prev) => !prev), [setLike]);

  return (
    <span onClick={toggleLike}>
      {(() => {
        if(liked){
          return (<img src="../images/iine-true.png" alt="" className="iine"/>);
        }else{
          return (<img src="../images/iine_false.png" alt="" className="iine"/>)
        }
      })()}
    </span>
  );
}

export default Like;