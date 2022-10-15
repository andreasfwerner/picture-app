<template>
    <div class="FileUploadDiv">
        <div class="FileUploadText">
          <div class="TextCenterDiv">  
            <h2>POST PHOTO</h2>
          </div> 
        </div>
        <div class="FileUploadButton">
            <input name="file" id="file" class="FileUploadInput inputfile" type="file" @change="onFileSelect" >
            <label for="file">SELECT IMAGE</label>
        </div>

        <div class="DescriptionField">
            <input type="text" v-model="description">
        </div>
        <div class="FilePostButton">
          <button class="glow-on-hover" @click="onUpload">UPLOAD</button>
        </div>
    </div>
</template>
  
  <script>
import axios from 'axios'

  export default {
    name: 'FileUpload',
    data(){
      return {
        selectedFile: null,
        description: null
      }
    }, props:{
      "id": Number
    },
    methods: {
      onFileSelect(event){
        this.selectedFile = event.target.files[0]
      },
      onUpload(){

        const date = new Date().toISOString().split('T')[0]

        const fd = new FormData();
        fd.append('image',this.selectedFile, this.selectedFile.name);
        fd.append('id',this.id);
        fd.append('date',date);
        fd.append('description',this.description);
        this.selectedFile = null;
        this.description = null;
        
        const path = "http://localhost:8080/post_posts"
        
        axios.post(path,fd)
        .then(res => {
          console.log(res)

        })
      
      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .FileUploadDiv{
    display: flex;
    width: 100%;
    height: 20%;
    background-color: black;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  .FileUploadText{
    width: 50%;
    text-align: center;
  }

  .FileUploadButton{
    display: flex;
    align-items: center;
    flex-direction: column;
    width: 60%;
  }
  .FileUploadInput{
    padding: 5%;
    width: 30%;

  }
  .FilePostButton{
    width: 20%;
    height: 20%;
  }
 
  .inputfile {
    width: 0.1px;
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    position: absolute;
    z-index: -1;
  }
  .inputfile + label {
    font-size: 0.9em;
    font-weight: 700;
    margin: 5%;
    color: white;
    background-color: black;
    display: inline-block;
}

.inputfile:focus + label,
.inputfile + label:hover {
    background-color: black;
}
.inputfile + label {
	cursor: pointer; /* "hand" cursor */
}
.glow-on-hover  {
  width: 100%;
  height: 100%;
  border: none;
  outline: none;
  color: #fff;
  background: #111;
  cursor: pointer;
  position: relative;
  z-index: 0;
  border-radius: 10px;
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

  h2{
    margin: auto;
    color: aliceblue;
  }

  </style>
  