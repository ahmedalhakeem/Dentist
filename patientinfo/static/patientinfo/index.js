document.addEventListener('DOMContentLoaded', function(){
   selectdate();
   document.querySelector('#next_appointment').style.display = 'none';
   document.querySelector('#next-date').addEventListener('click', ()=>{
       document.querySelector('#next_appointment').style.display = 'block';
       });
       
   }) 

function selectdate(){
    $('#select-date').datepicker({
        numberOfMonths:1,
        changeMonth: true,
        changeYear: true,
        showOtherMonths:true,
        minDate: new Date(2009, 0, 1),
        maxDate : new Date(2025, 11,31),
        dateFormat : 'yy-mm-dd' 
        })
}

    