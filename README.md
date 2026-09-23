# FixTrack

FixTrack is a lightweight repair job tracking application built with Flask and SQLAlchemy.

I made it mainly to track the repairs I make as a Luthier.

It is a work in progress that grows with my needs on a day to day with this work.

## Features

* Create repair jobs
* View all repairs
* View repair details
* Edit repair information
* Update repair status
* Delete repairs
* Persistent storage with SQLite

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Jinja2
* HTML

## Installation

Clone the repository:

```bash
git clone https://github.com/JuanEscalada/fixtrack.git
cd fixtrack
```

Install the dependencies using `uv`:

```bash
uv sync
```

Run the application:

```bash
uv run flask --app run run --debug
```

Then open:

```text
http://127.0.0.1:5000
```

## Repair Statuses

Repairs can currently use the following statuses:

* Received
* Diagnosing
* Waiting for parts
* In progress
* Ready
* Delivered
* Cancelled

## Current Scope

FixTrack is intentionally kept small and it is a work in progress.

Possible future improvements include:

* Search and filtering
* Parts Inventory
* Parts I need Inventory
* Customer management
* Cost tracking
* Automated tests

More technical improvements could be:

* PostgreSQL support
* REST API
* Docker support
* Deployment

If the need to deploy on a more professional environment arises.

## License

This project is available for educational and portfolio purposes.