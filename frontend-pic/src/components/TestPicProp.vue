<template>
    <div class="Image">
        <div class="picture">
            <img ref="image">
        </div>
    </div>

</template>
  
<script>

  export default {
    name: 'TestPicProp',
    
    data(){
        return{
            src:null,
        }
    },
    methods:{
        updateSrc(src){
            this.$refs.image.src=src
        }
    }
  }
</script>

<style>

    .pic{
        width: 400px;
        height: 400px;
        background-color: blue;
    }
</style>
  