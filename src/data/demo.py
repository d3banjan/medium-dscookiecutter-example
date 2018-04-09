import os, click, logging

@click.group()
def meta_command():
    pass

@click.command()
@click.option('--option',default='default')
@click.argument('string',nargs=-1)
def first(option,string):
    print("the argument(s) is(are) \"{}\" with an optional modifier {}".format(",".join(string),option))

@click.command()
@click.option('--option',default='default')
@click.argument('string',nargs=-1)
def second(option,string):
    print("the argument(s) is(are) \"{}\" with an optional modifier {}".format(",".join(string),option))

meta_command.add_command(first)
meta_command.add_command(second)

if __name__=='__main__':
    meta_command()

