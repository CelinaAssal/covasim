from unittest_support import CovaTest, TProps

TPKeys = TProps.ParKeys.SimKeys


class PopulationTypeTests(CovaTest):
    def setUp(self):
        super().setUp()
        pass

    def tearDown(self):
        super().tearDown()
        pass

    def test_different_pop_types(self):
        pop_types = ['random', 'hybrid']  #, 'synthpops']
        results = {}
        short_sample = {
            TPKeys.number_agents: 1000,
            TPKeys.number_simulated_days: 10,
            TPKeys.initial_infected_count: 50
        }
        for poptype in pop_types:
            self.run_sim(short_sample, population_type=poptype)
            results[poptype] = self.simulation_result['results']
            pass
        self.assertEqual(len(results), len(pop_types))
        for k in results:
            these_results = results[k]
            self.assertIsNotNone(these_results)
            day_0_susceptible = these_results[TProps.ResKeys.susceptible_at_timestep][0]
            day_0_exposed = these_results[TProps.ResKeys.exposed_at_timestep][0]

            self.assertEqual(day_0_susceptible + day_0_exposed, short_sample[TPKeys.number_agents],
                             msg=f"Day 0 population should be as specified in params. Poptype {k} was different.")
            self.assertGreater(these_results['cum_infections'][-1],
                               these_results['cum_infections'][0],
                               msg=f"Should see infections increase. Pop type {k} didn't do that.")
            self.assertGreater(these_results['cum_symptomatic'][-1],
                               these_results['cum_symptomatic'][0],
                               msg=f"Should see symptomatic counts increase. Pop type {k} didn't do that.")

