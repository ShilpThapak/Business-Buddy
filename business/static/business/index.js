document.addEventListener('DOMContentLoaded', main)

function main(){
    console.log('js file working!');

    leadform = document.querySelector('#leadform');
    leadform.onsubmit =()=>{
        console.log('submit button clicked');
        leadname = document.querySelector('#leadname').value;
        leademail = document.querySelector('#leademail').value;
        leadnumber = document.querySelector('#leadnumber').value;
        leadinterest = document.querySelector('#leadinterest').value;

        console.log(leadname, leademail, leadnumber, leadinterest);
        
        form = new FormData();
        form.append("leadname", leadname);
        form.append('leademail', leademail);
        form.append('leadnumber', leadnumber);
        form.append('leadinterest', leadinterest);

        fetch('/savelead', {
            method: 'POST',
            body: form
        })
        
        document.querySelector('#leadname').value= "";
        document.querySelector('#leademail').value= "";
        document.querySelector('#leadnumber').value= "";

        document.querySelector('#blankdiv').style.display = 'none';
        document.querySelector('#messagediv').style.display = 'block';
        return false;
    }
}