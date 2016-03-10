from flask import Flask, render_template, request, abort, session, redirect, url_for, Response
from flask.ext.mysqldb import MySQL
from isithealing import views

import os
import json
import string
