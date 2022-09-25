## Task 4 -- Jenkins
**Create a Jenkins pipeline**

 1. Create a Jenkins pipeline in which you download the necessary scripts and files from a GitHub repository and install the service from task 3 in a docker container.
 2. Take screenshots indicating the success of your actions and save script files.

Resources 

 - NTP-server [[cturra/docker-ntp: 🕒 Chrony NTP Server running in a Docker container (without the priviledged flag) (github.com)](https://github.com/cturra/docker-ntp)](https://github.com/cturra/docker-ntp)
 - Jenkins [https://www.jenkins.io/doc/book/installing/linux/](https://www.jenkins.io/doc/book/installing/linux/)
 - Docker [[Install Docker Engine on Ubuntu | Docker Documentation](https://docs.docker.com/engine/install/ubuntu/)(https://docs.docker.com/engine/install/ubuntu/)
 - [Fix the Jenkins Docker error: Permission denied when trying to connect to Docker daemon - Coffee Talk: Java, News, Stories and Opinions (theserverside.com)](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Fix-Jenkins-Docker-Permission-denied-daemon-error)
 - [jenkins - Git PullRequest job failed. Couldn't find any revision to build. Verify the repository and branch configuration for this job - Stack Overflow](https://stackoverflow.com/questions/23906352/git-pullrequest-job-failed-couldnt-find-any-revision-to-build-verify-the-repo)

Fork **Github** repository from resource to my **Github** because for **Jenkins** to pull repository from **Github** it need credential which is impossible to acquire from the original repository.

After setup **Jenkins**, we can access it with it web app to create new pipeline.

**Jenkins** web app interface

![9](https://user-images.githubusercontent.com/46795818/192136658-4096b305-1508-4160-9488-075c1ed6fa0d.png)


Result from working pipeline

![10](https://user-images.githubusercontent.com/46795818/192136665-0c3cc76d-e596-4289-b3ad-af4075142ca2.png)

Task preparation:

 - Linux VM
 - Docker
 - Jenkins

Task implement
Using Jenkins to create a pipeline that download the necessary scripts and files from a GitHub repository and install the service in a docker container

Task troubleshooting

 - Docker syntax, Jenkins Docker permission.
 - Jenkins installation process, how to crate pipeline, syntax
 - How to acquire Github credential for Jenkins
