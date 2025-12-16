1

class FuzzyDoseSystem:
    def __init__(self):
        # Ορισμός ασαφών συνόλων για θερμοκρασία (T) και δόση (D)
        self.T = {
            'LOW': {37: 0.2, 37.5: 1, 38: 0.5, 38.5: 0.2, 39: 0, 39.5: 0, 40: 0},
            'HIGH': {37: 0, 37.5: 0, 38: 0.2, 38.5: 0.5, 39: 0.8, 39.5: 1, 40: 1}
        }

        self.D = {
            'LOW': {0: 1, 2: 0.8, 5: 0.5, 8: 0.2, 10: 0},
            'HIGH': {0: 0, 2: 0.2, 5: 0.5, 8: 0.8, 10: 1}
        }

        # Εναλλακτικά σύνολα (προαιρετικά)
        self.T_alt = {
            'LOW': {37: 0.3, 37.5: 0.9, 38: 0.6, 38.5: 0.3, 39: 0.1, 39.5: 0, 40: 0},
            'HIGH': {37: 0, 37.5: 0.1, 38: 0.3, 38.5: 0.6, 39: 0.9, 39.5: 1, 40: 1}
        }

        self.D_alt = {
            'LOW': {0: 1, 2: 0.7, 5: 0.4, 8: 0.1, 10: 0},
            'HIGH': {0: 0, 2: 0.3, 5: 0.6, 8: 0.9, 10: 1}
        }

        self.current_sets = 'default'
        self.inference_method = 'MIN'  # 'MIN' ή 'PRODUCT'

    def set_sets(self, sets_type):
        self.current_sets = sets_type

    def set_inference_method(self, method):
        self.inference_method = method

    def get_membership(self, value, fuzzy_set):
        """Υπολογισμός βαθμού συμμετοχής με γραμμική παρεμβολή"""
        keys = sorted(fuzzy_set.keys())
        if value <= keys[0]:
            return fuzzy_set[keys[0]]
        if value >= keys[-1]:
            return fuzzy_set[keys[-1]]

        lower = max(k for k in keys if k <= value)
        upper = min(k for k in keys if k > value)
        ratio = (value - lower) / (upper - lower)
        return fuzzy_set[lower] + ratio * (fuzzy_set[upper] - fuzzy_set[lower])

    def apply_inference(self, rule_strength, output_set):
        """Εφαρμογή MIN ή PRODUCT για την 'κόψιμο' των συναρτήσεων εξόδου"""
        if self.inference_method == 'MIN':
            return {d: min(rule_strength, m) for d, m in output_set.items()}
        elif self.inference_method == 'PRODUCT':
            return {d: rule_strength * m for d, m in output_set.items()}

    def calculate_dose(self, temperature):
        # Επιλογή συνόλων
        if self.current_sets == 'default':
            T_LOW = self.T['LOW']
            T_HIGH = self.T['HIGH']
            D_LOW = self.D['LOW']
            D_HIGH = self.D['HIGH']
        else:
            T_LOW = self.T_alt['LOW']
            T_HIGH = self.T_alt['HIGH']
            D_LOW = self.D_alt['LOW']
            D_HIGH = self.D_alt['HIGH']

        # Βήμα 1: Fuzzification (Υπολογισμός βαθμών συμμετοχής)
        low_degree = self.get_membership(temperature, T_LOW)
        high_degree = self.get_membership(temperature, T_HIGH)

        # Βήμα 2: Εφαρμογή κανόνων με επιλεγμένη μέθοδο (MIN/PRODUCT)
        # Κανόνας 1: IF T is HIGH THEN D is HIGH
        rule1_output = self.apply_inference(high_degree, D_HIGH)

        # Κανόνας 2: IF T is LOW THEN D is LOW
        rule2_output = self.apply_inference(low_degree, D_LOW)

        # Βήμα 3: Συνένωση (aggregation) με MAX
        aggregated = {}
        all_doses = set(D_LOW.keys()).union(set(D_HIGH.keys()))
        for d in all_doses:
            m1 = rule1_output.get(d, 0)
            m2 = rule2_output.get(d, 0)
            aggregated[d] = max(m1, m2)  # Union με MAX

        # Βήμα 4: Αποασαφοποίηση (κέντρο βάρους)
        numerator = sum(d * m for d, m in aggregated.items())
        denominator = sum(m for d, m in aggregated.items())
        return numerator / denominator if denominator != 0 else 0

def main():
    system = FuzzyDoseSystem()

    print("Σύστημα Ασαφούς Λογικής για Υπολογισμό Φαρμακευτικής Δόσης")
    print("--------------------------------------------------------")

    # Επιλογή συνόλων
    sets_choice = input("Επιλέξτε ασαφή σύνολα (1: Προκαθορισμένα, 2: Εναλλακτικά): ")
    if sets_choice == "2":
        system.set_sets("alternative")

    # Επιλογή μεθόδου συμπερασμού
    method_choice = input("Επιλέξτε μέθοδο συμπερασμού (1: MIN, 2: PRODUCT): ")
    if method_choice == "2":
        system.set_inference_method("PRODUCT")

    # Εισαγωγή θερμοκρασίας
    while True:
        try:
            temp = float(input("Εισάγετε τη θερμοκρασία του ασθενούς (37-40°C): "))
            if 37 <= temp <= 40:
                break
            print("Παρακαλώ εισάγετε τιμή μεταξύ 37 και 40.")
        except ValueError:
            print("Παρακαλώ εισάγετε έναν αριθμό.")

    # Υπολογισμός και εμφάνιση δόσης
    dose = system.calculate_dose(temp)
    print(f"\nΣυνιστώμενη δόση ({system.inference_method} method): {dose:.2f} μονάδες")

if __name__ == "__main__":
    main()