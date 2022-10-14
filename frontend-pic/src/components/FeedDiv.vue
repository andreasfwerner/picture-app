<template>
    <div class="FeedDiv">
        <FeedPicture :pic_url="pic_url"
                    :username="username"
                    :date_posted="todaysDate"
                    :description="description"
                    :username_pic="username_pic">
        </FeedPicture>
        <CommentDiv>
          
        </CommentDiv>
    </div>
</template>
  
  <script>
  import FeedPicture from './FeedPicture.vue'
  import CommentDiv from './CommentDiv.vue'
  export default {
    name: 'FeedDiv',
    components: {
        FeedPicture,
        CommentDiv
    },
    data(){
        return{
            todaysDate: new Date().toISOString().split('T')[0],
            description: "OMG what a nice picture",
            username:"vuesername",
            pic_url:require("../../test_data/logo.png"),
            username_pic:require("../../test_data/logo.png")
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .FeedDiv{
    width: 100%;
    height: 80%;
    background-color: black;
  }
  
  </style>
  