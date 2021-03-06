
User Story:
-----------
User Story: Draft basic OPERANDI setup with concrete tools/technology/software

Aim of user story:
- get better understanding of targeted architecture
- transfer architecture to be able to start programming components

Starting Point
--------------
![picture operandi-overview missing](operandi-overview.png)

Simplify
--------
![picture operandi-draft missing](operandi-draft.png)

Components:
-----------

Harvester:
- used to get all books from VD-18
- OAI-PMH
- Server for VD-18 not available to us yet
- could not further explore / try as i wanted to because OAI-PMH not available

REST-API:
- Flask, FastAPI
- needed for OCR-D WebAPI as well
- needed to create OCR-Request
- Producer for RabbitMQ

OCR-Request:
- ID of work to be OCRed?
- path to metsfile?
- fileGroup?

RabbitMQ:
- used to queue jobs

Service Broker:
- Part of `Main Service`, or background-job?
- Python Class (or background-job)
- Interface to HPC:
    - one way (or can HPC send Data/Results via SSH)?
    - submits SSH-Jobs to HPC
    - send data (Images for OCR-Request) via SSH (rsync, scp) to HPC
    - receive results from HPC:
        - periodically look for finished jobs and fetch data (results)
- Reads from Rabbit-MQ (Consumer)


Questions:
----------
- Is there already a OAIPMH server available for VD-18?
- How to get Images to HPC or to the Service Broker to send them to HPC?
- Harvester: Run in background? Schedule periodically with Flask/FastAPI?
