import gitlab



def generate_client(token, server):
    client =  gitlab.Gitlab(server, private_token=token, keep_base_url=True)
    client.auth()
    
    return(client)