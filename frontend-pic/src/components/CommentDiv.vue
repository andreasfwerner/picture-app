<template>
    <div class="CommentDiv">
      <div class="comments">
        <CommentProp v-for="(comment,index) in comments" :key="index"
          :username="comment.username"
          :user_img="comment.user_img"
          :user_comment="comment.user_comment"
        ></CommentProp>
        

      </div>
      <div class="Scroller">
        <div class="UpButton">
            <a>
                <img class="ArrowUp" src="../../svg/arrowdown.svg" />
            </a>
        </div>
        <div class="DownButton">
             <a>
                <img class="ArrowDown" src="../../svg/arrowdown.svg" />
            </a>
        </div>
      </div>
    </div>
</template>
  
  <script>
  import CommentProp from './Comment.vue'
  export default {
    name: 'CommentDiv',
    components:{
      CommentProp
    },
    data(){
      return{
        comments:[
        {
        username:"andreasf",
        user_img:require("../../test_data/logo.png"),
        user_comment:"what a lovly picture"
        },
        {
        username:"noafink",
        user_img:require("../../test_data/logo.png"),
        user_comment:"ugly ahh picture"
        }
        ],

      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .CommentDiv{
      width: 100%;
      height: 29.5%;
      background-color: gold;
      display: flex;
      flex-direction: row;
      
    }
    .comments{
      height: 100%;
      width: 100%;
      display: flex;
      flex-direction: column;
    }
    .Scroller{
      width: 5%;
      height: 100%;
      background-color: black;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .ArrowDown{
      transform: rotate(180deg);
  }
  .DownButton{
    width: 90%;
    height: 25%;
  }
  .UpButton{
    width: 90%;
    height: 25%;
  }
  </style>
  