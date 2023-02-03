def get_spent_calories(self) -> float:
    return ((self.CALORIES_MEAN_SPEED_MULTIPLIER
            * self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
            * self.weight / self.M_IN_KM * self.duration
            )
