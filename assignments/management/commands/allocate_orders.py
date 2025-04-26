from django.core.management.base import BaseCommand
from django.utils import timezone
from assignments.models import Warehouse, Agent, Order
from itertools import cycle

class Command(BaseCommand):
    help = 'Allocate unassigned orders to agents based on capacity and compliance rules'

    def handle(self, *args, **options):
        today = timezone.now().date()
        for warehouse in Warehouse.objects.all():
            agents = list(warehouse.agents.all())
            orders = Order.objects.filter(warehouse=warehouse, assigned=False)
            if not agents:
                continue
            self.stdout.write(f"Allocating for {warehouse.name}: {orders.count()} orders, {len(agents)} agents")
            agent_cycle = cycle(agents)
            for order in orders:
                for _ in agents:
                    agent = next(agent_cycle)
                    # TODO: implement detailed capacity check (hours and distance)
                    daily_orders = agent.orders.filter(created_at__date=today).count()
                    if daily_orders < 60:  # simple cap; refine using time/distance
                        order.assigned_agent = agent
                        order.assigned = True
                        order.save()
                        break
            self.stdout.write(self.style.SUCCESS(f"Completed allocation for {warehouse.name}"))