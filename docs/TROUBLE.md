#Things that caused me trouble..
1. Getting the AWS credentials inside docker, I got it eventually... used an external env file for the docker-compose and used
environment variables in travis, and when needed used "-e" in docker with the variables.

2. Doing the tests, was trying to do simple test with curl... can't make it work, getting problems with auth.

3. Not really sure what was I suppose to do with the "healty" check... 'container' or <LINK_TO_HUB> so I just hardcoded the dockerhub link.
