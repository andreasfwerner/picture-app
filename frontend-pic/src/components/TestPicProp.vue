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
    
    props:{
        pic_src: String
    }
    ,
    methods:{
        updateSrc(){
            console.log(this.pic_src)
            this.$refs.image.src=this.pic_src
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
  