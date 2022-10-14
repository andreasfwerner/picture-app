<template>
    <div class="Comment">
        <div class="UserInfoDiv">
            <div class="CommentUsername">{{username}}</div>
            <div class="CommentPicture">
              <img :src="user_img"/>
            </div>
        </div>
            <div class="CommentText">{{user_comment}}</div>    
    </div>

</template>
  
  <script>
  export default {
    name: 'CommentProp',
    props:{
        "username": String,
        "user_img": String,
        "user_comment": String
        }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .Comment{
      height: 50%;
      width: 100%;
      background-color: red;
      display:flex;
      flex-direction: column;
    }
    .UserInfoDiv{
      width: 100%;
      height: 30%;
      display: flex;
      flex-direction: row;
      background-color:gray ;
      align-items: center ;
    }
    .CommentPicture{
      width: 1.5em;
      height: 1.5em;
      border-radius: 50%;
      background-color: black;

    }
    img{
      width: 1.5em;
      height:1.5em;
      border-radius: 50%;
    }
    .CommentUsername{
      width:  90%;
      height: 100%;
    }
    .CommentText{
      width: 100%;
      height: 90%;
      color: white;
      background-color: black;
    }
    

  </style>
  