# Helpdesk Tickets System

tickets = [{"id": 1, "user": "Malek", "issue": "Network", "status": "Open"}]

def create_ticket(user, issue):
    global tickets
    ticket_id = max([t['id'] for t in tickets], default=0) + 1
    tickets.append({"id": ticket_id, "user": user, "issue": issue, "status": "Open"})
    return ticket_id

def get_all_tickets():
    return tickets

def get_tickets_by_status(status):
    return [t for t in tickets if t['status'] == status]

def resolve_ticket(ticket_id):
    for t in tickets:
        if t['id'] == ticket_id:
            t['status'] = "Closed"
            return True
    return False

def search_tickets_by_user(user):
    return [t for t in tickets if t['user'] == user]

def update_issue_desc(ticket_id, new_desc):
    for t in tickets:
        if t['id'] == ticket_id:
            t['issue'] = new_desc
            return True
    return False

def count_open_tickets():
    return len([t for t in tickets if t['status'] == "Open"])

def delete_ticket(ticket_id):
    global tickets
    tickets = [t for t in tickets if t['id'] != ticket_id]