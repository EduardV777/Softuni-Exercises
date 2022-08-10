from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:
    
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_plan(self, plan: ExercisePlan):
        for k in range(0, len(self.plans)):
            if self.plans[k].id == plan.id:
                return -1

        self.plans.append(plan)

    def add_customer(self, customer: Customer):
        for k in range(0, len(self.customers)):
            if self.customers[k].id == customer.id:
                return -1

        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        for k in range(0, len(self.trainers)):
            if self.trainers[k].id == trainer.id:
                return -1

        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        for k in range(0, len(self.equipment)):
            if self.equipment[k].id == equipment.id:
                return -1

        self.equipment.append(equipment)

    def add_subscription(self, subscription: Subscription):
        for k in range(0, len(self.subscriptions)):
            if self.subscriptions[k].id == subscription.id:
                return -1

        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        selectSub = 0
        selectCustomer = 0
        selectTrainer = 0
        selectPlan = 0
        selectEquipment = 0

        for k in range(0, len(self.subscriptions)):
            if self.subscriptions[k].id == subscription_id:
                selectSub = self.subscriptions[k]
                break
        
        customerId = selectSub.customer_id
        exPlanId = selectSub.exercise_id
        trainerId = selectSub.trainer_id

        for k in range(0, len(self.customers)):
            if self.customers[k].id == customerId:
                selectCustomer = self.customers[k]
                break

        for k in range(0, len(self.plans)):
            if self.plans[k].id == exPlanId:
                selectPlan = self.plans[k]
                equipmentId = selectPlan.equipment_id
                break
        
        for k in range(0, len(self.trainers)):
            if self.trainers[k].id == trainerId:
                selectTrainer = self.trainers[k]
            
        for k in range(0, len(self.equipment)):
            if self.equipment[k].id == equipmentId:
                selectEquipment = self.equipment[k]

        output = selectSub.__repr__() + "\n"
        output += selectCustomer.__repr__() + "\n"
        output += selectTrainer.__repr__() + "\n"
        output += selectEquipment.__repr__() + "\n"
        output += selectPlan.__repr__()

        return output