import typer
import pyperclip
from db import initialize_db, add_password, get_password, get_all_passwords, delete_all_passwords
from crypto_utils import generate_master_key, encrypt_data, decrypt_data
from password_utils import generate_password
from typer import Option

app = typer.Typer()
cipher = generate_master_key()

@app.command()
def init():
    """Initialize the database."""
    initialize_db()
    typer.echo("Password manager initialized!!")

@app.command()
def add(
    service: str = Option(..., help="The service for which the password is being added."),
    username: str = Option(..., help="The username for the service."),
    password: str = Option(None, help="The password for the service. If not provided, one will be generated.")
):
    """Add a new password."""
    if not password:
        password = generate_password()  # Generate password if not provided
    encrypted_password = encrypt_data(password, cipher)
    add_password(service, username, encrypted_password)
    typer.echo(f"Password for {service} added.")

@app.command()
def get(
    service: str = Option(..., help="The service for which you want the password."),
):
    """Retrieve a password."""
    try:
        results = get_password(service)
        if results:
            toCopy=True
            for username, encrypted_password in results:
                password = decrypt_data(encrypted_password, cipher)
                typer.echo(f"Service: {service}\nUsername: {username}\nPassword: {password}")
                
                if(toCopy):
                    # Copy the password to the clipboard
                    pyperclip.copy(password)
                    typer.echo("Password copied to clipboard.")
                    toCopy = False
                
                typer.echo("-" * 40)  # separator for better readability
        else:
            typer.echo(f"No password found for {service}.")
    except Exception as e:
        typer.echo(f"An error occurred: {e}")


@app.command()
def delete(
    service: str = Option(..., help="The service for which you want the password to be deleted."), 
    username: str = Option(..., help="The username under SERVICE for which you want the password to be deleted.")
):
    """Delete a password entry for a specific service and username."""
    delete_password(service, username)
    typer.echo(f"Password for {username} under service {service} has been deleted.")


@app.command()
def getall():
    results = get_all_passwords()
    if results:
        for service, username, encrypted_password in results:
            password = decrypt_data(encrypted_password, cipher)
            typer.echo(f"Service: {service}")
            typer.echo(f"Username: {username}")
            typer.echo(f"Password: {password}")
            typer.echo("-" * 40)  # separator for better readability
    else:
        typer.echo("No passwords found!")

@app.command()
def deleteall():
    delete_all_passwords()
    typer.echo("All passwords have been deleted.")

@app.command()
def generate(
    length: int = Option(16, help="The length of the password to be generated."),
):
    """Generate a random password."""
    password = generate_password(length)
    typer.echo(f"Generated password: {password}")

if __name__ == "__main__":
    app()
