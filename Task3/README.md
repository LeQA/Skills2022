## Task 3 -- Docker
**Create a docker microservice.**

 1. Create a docker “ntp service”
 2. Adapt configuration elements according to your network context
 3. Take screenshots indicating the success of your actions and save script files and related docs.

Resource [https://github.com/cturra/docker-ntp](https://github.com/cturra/docker-ntp)

Pull docker image with command 

`docker pull cturra/ntp`

![6](https://user-images.githubusercontent.com/46795818/192135491-988ca2d8-7829-428f-b1a3-9201be96c98b.png)

Run docker image

`docker compose up -d ntp`

![7](https://user-images.githubusercontent.com/46795818/192135632-b4ed1a12-2764-485e-8af5-a305831211f4.png)

Docker image running log

![8](https://user-images.githubusercontent.com/46795818/192135888-6df4edd7-9df7-4ffd-a4e4-0feaae5ab603.png)

Task preparation:

 - Linux VM
 - Docker

Task implement

 - Running ntp server using docker

Task troubleshooting

 - Docker syntax
