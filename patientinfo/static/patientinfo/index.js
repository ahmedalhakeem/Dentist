document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.next_date').style.display = "none";
    document.querySelector('#show-next').addEventListener('click', ()=>{
        document.querySelector('.next_date').style.display = "block";
        

    })
})