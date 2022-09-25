## Task 2 -- Ansible Skills Test

**Write the Ansible script to install and test the websever with ping command in a single playbook. Choose either Apache or Nginx server based on your own preference.**

 1. Name the playbook WEBSERVER INSTALLATION AND TESTING.
 2. Take screenshots indicating the success of your actions and save script files and related docs.

Running ansible playbook with command 
`ansible-playbook WEBSERVER_INSTALLATION_AND_TESTING.yml -K`

![3](https://user-images.githubusercontent.com/46795818/192132627-e8600868-5885-47a4-92fa-d80db4953ac6.png)

Website at localhost after running the playbook

![5](https://user-images.githubusercontent.com/46795818/192132648-189415d0-730b-441d-8fb9-c5dd8ef50582.png)

Task preparation:

 - Linux VM
 - Anisble
 - Apache2

Task implement
Ansible playbook run on localhost that automatically

 - install apache2, 
 - start apache2 server, 
 - push user create index html to apache server 
 - ping server with ansible built in ping tool and ping command

Task troubleshooting

 - write ansible playbook in correct yaml format
 - implement apt and ping function in ansible playbook
