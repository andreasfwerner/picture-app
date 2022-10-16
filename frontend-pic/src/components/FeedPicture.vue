<template>
    <div class="PictureWrapper">
        <div class="TopDiv">
            <div class="PictureDiv">
                <img class="FeedPic" ref="image" alt="Description of image"/>
            </div>
            <div class="UserDiv">
                <div class="UserPicDiv">
                </div>
                <div class="UsernameDiv">
                    <h3>{{name}}</h3>
                </div>
            </div>
        </div>
        <div class="DescriptionDiv">
            <text>{{description}}</text>
        </div>
        <div class="BottomDiv">
            <div class="DateDiv">
                <div>Posted: {{date_posted}}</div>
            </div>
            <div class="FillDiv"></div>
            <div class="DeleteDiv">
                <button class="glow-on-hover">Delete</button>
            </div>
        </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'FeedPicture',
    props:{
        description: String,
        date_posted: String,
        pic_src: String,
        name: String
    },
    methods:{
        updateSrc(){
            this.$refs.image.src=this.pic_src
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .PictureWrapper{
    display: flex;
    flex-direction: column;
    width: 100;
    height: 70%;
    background-color: black;
    align-items: center;
    justify-content: center;
    border: 1px solid white;
  }
 
  .TopDiv{
    width: 80%;
    height: 50%;
    background-color: black;
    display: flex;
    flex-direction: row;
    
  }
        .PictureDiv{
            width: 70%;
            height:100%;
            background-color: black;
        }

                .FeedPic{

                    max-width:100%;
                    max-height:100%;
                    height: auto;
                    border:1px solid white;
                }
        .UserDiv{
            width: 30%;
            height: 100%;
            background-color: black;
            display: flex;
            flex-direction: column;
        }

                .UserPicDiv{
                    width: 100%;
                    height: 30%;
                    background-color: black;
                }  
                        .CircleDiv{
                            width:  4em;
                            height: 4em;
                            background-color: black;
                            border-radius: 50%;
                        }
                            .ProfilePic{
                                max-width:100%;
                                max-height:100%;
                                height: auto;
                                border-radius: 50%;
                            }
                .UsernameDiv{
                    width: 100%;
                    height: 40%;
                    background-color: black;
                    color: white
                }
        
  .DescriptionDiv{
    width: 80%;
    height: 20%;
    background-color: black;
    color: white;
  }


  .BottomDiv{
    width: 80%;
    height: 10%;
    background-color: maroon;
    display: flex;
    flex-direction: row;
}
        .DateDiv{
            width: 30%;
            height: 100%;
            background-color: black;
            color: white;
        }
        .FillDiv{
            width: 50%;
            height: 100%;
            background-color: black;
        }
        .DeleteDiv{
            width: 20%;
            height: 100%;
            background-color: black;
        }
        .glow-on-hover  {
            width: 80%;
            height: 80%;
            border: none;
            outline: none;
            color: #fff;
            background: #111;
            cursor: pointer;
            position: relative;
            z-index: 0;
            border-radius: 10px;
            margin-top: 4%;
          }
          
          .glow-on-hover:before {
            content: '';
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            position: absolute;
            top: -2px;
            left:-2px;
            background-size: 400%;
            z-index: -1;
            filter: blur(5px);
            width: calc(100% + 4px);
            height: calc(100% + 4px);
            animation: glowing 20s linear infinite;
            opacity: 0;
            transition: opacity .3s ease-in-out;
            border-radius: 10px;
          }
          
          .glow-on-hover:active {
            color: #000
          }
          
          .glow-on-hover:active:after {
            background: transparent;
          }
          
          .glow-on-hover:hover:before {
            opacity: 1;
          }
          
          .glow-on-hover:after{
            z-index: -1;
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background: #111;
            left: 0;
            top: 0;
            border-radius: 10px;
          }
          
          
          @keyframes glowing {
            0% { background-position: 0 0; }
            50% { background-position: 400% 0; }
            100% { background-position: 0 0; }
          }
  </style>
  