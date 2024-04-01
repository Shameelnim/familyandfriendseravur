 // First one
 const observe = new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('oneshow')
        }
        else{
            entry.target.classList.remove('oneshow')
        }
    })
})
const one = document.querySelectorAll('.one');
one.forEach((el)=>observe.observe(el))

 // Second one
 const ob = new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('twoshow')
        }
        else{
            entry.target.classList.remove('twoshow')
        }
    })
})
const two = document.querySelectorAll('.two');
two.forEach((el)=>observe.observe(el))