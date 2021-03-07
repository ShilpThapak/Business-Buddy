document.addEventListener('DOMContentLoaded', main);

function main(){
    console.log('js file working!');

    var permission = document.querySelector('#permission').innerHTML;
    console.log(permission);

    if (permission==1){
        reassigndiv = document.querySelector('#reassigndiv');
        reassigndiv.style.display = 'none';
        var editlink = document.querySelector('#editlink')
        editlink.onclick = edit;
        
        function edit(){
            console.log("edit link clicked!")
            associatediv = document.querySelector('#assignedto');
            associatediv.style.display = 'none';
            reassigndiv.style.display = 'block';
            return false;
        }

        var assignform = document.querySelector('#assignform');
        assignform.onsubmit = () =>{
            console.log('submit button clicked!');
            userid = document.querySelector('#selectoption').value;
            leadid = document.querySelector('#leadid').innerHTML;
            console.log(userid);
            console.log(leadid);

            form = new FormData();
            form.append("userid", userid);
            form.append("leadid", leadid);

            fetch('/business-buddy/sales/assign', {
                method: 'POST',
                body: form
            })
            .then(response => response.json())
            .then(data=> {
                console.log(data);
                associatediv = document.querySelector('#assignedto');
                associatediv.innerHTML = `${data.associate} &emsp;`;
                a = document.createElement('A')
                a.innerHTML = 'Edit';
                a.setAttribute("href", "")
                a.id = "editlink";
                a.onclick = edit;
                associatediv.append(a);

            })

            associatediv.style.display = 'block';
            reassigndiv.style.display = 'none';
            return false;
        }
    }
    else{
        reassigndiv.style.display = 'none';
    }
    

    var statusEditLink = document.querySelector('#status-edit-link');
    statusEditLink.onclick = editstatus;
    
    function editstatus() {
        console.log('status edit link clicked');

        var editStatusDiv = document.querySelector('#edit-status-div');
        editStatusDiv.style.display = 'inline';

        var leadStatusDiv =document.querySelector('#lead-status-div');
        leadStatusDiv.style.display = 'none';

        var statusForm = document.querySelector('#statusform');
        statusForm.onsubmit = () => {
            console.log('submit button clicked!');
            
            leadid = document.querySelector('#leadid').innerHTML;
            console.log(leadid);

            newstatus = document.querySelector('#status-select-option').value;
            console.log(newstatus);


            form = new FormData();
            form.append("leadid", leadid);
            form.append("newstatus", newstatus);

            fetch('/business-buddy/sales/editstatus', {
                method: 'POST',
                body: form
            })
            .then(response => response.json())
            .then(data=> {
                console.log(data);
                leadStatusDiv.innerHTML = `${data.newtext} &emsp;`;
                a = document.createElement('A')
                a.innerHTML = 'Edit';
                a.setAttribute("href", "")
                a.id = "editlink";
                a.onclick = editstatus;
                leadStatusDiv.append(a);
            })

            leadStatusDiv.style.display = 'inline';
            editStatusDiv.style.display = 'none';
 
            return false;
        }

        return false;
    }
    




    tasksbtn = document.querySelector('#tasksbtn');
    tasksbtn.onclick = () =>{
        console.log('task button clicked');
        taskscol = document.querySelector('#taskscol');
        console.log(taskscol);
        taskscol.classList.add('active');
        overlay = document.querySelector('#overlay');
        console.log(overlay);
        overlay.classList.add('active');
    }

    closebtn = document.querySelector('.close-button');
    closebtn.onclick = () =>{
        console.log('close button clicked');
        overlay.classList.remove('active');
        taskscol.classList.remove('active');
    }

    donebtn = document.querySelectorAll('#donebtn');
    donebtn.forEach(donebtn => {
        donebtn.onclick = ()=> {
            console.log("done button clicked! right");
            console.log(donebtn.parentElement.parentElement.parentElement);
            taskdiv = donebtn.parentElement.parentElement.parentElement;
            taskid = taskdiv.children[0].value
            
            //fetch('/task')

            form = new FormData();
            form.append("taskid", taskid);

            fetch("/taskdone", {
                method: 'POST',
                body: form
            })

            taskdiv.style.display = 'none';
        }
    })

}