"""
Tests of the common implementation of the simulation control functions, using
the pyNN.mock backend.

:copyright: Copyright 2006-2013 by the PyNN team, see AUTHORS.
:license: CeCILL, see LICENSE for details.
"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest
import pyNN.mock as sim    

try:
    from mpi4py import MPI
except ImportError:
    MPI = None

if MPI:
    mpi_comm = MPI.COMM_WORLD

class TestSimulationControl(unittest.TestCase):
    def test_setup(self):
        self.assertRaises(Exception, sim.setup, min_delay=1.0, max_delay=0.9)
        self.assertRaises(Exception, sim.setup, mindelay=1.0)  # } common
        self.assertRaises(Exception, sim.setup, maxdelay=10.0) # } misspellings
        self.assertRaises(Exception, sim.setup, dt=0.1)        # }
        self.assertRaises(Exception, sim.setup, timestep=0.1, min_delay=0.09)

    def test_end(self):
        sim.setup()
        sim.end() # need a better test
    
    def test_run(self):
        sim.setup()
        self.assertEqual(sim.run(1000.0), 1000.0)
        self.assertEqual(sim.run(1000.0), 2000.0)
    
    def test_reset(self):
        sim.setup()
        sim.run(1000.0)
        sim.reset()
        self.assertEqual(sim.get_current_time(), 0.0)
    
    def test_current_time(self):
        sim.setup(timestep=0.1)
        sim.run(10.1)
        self.assertEqual(sim.get_current_time(), 10.1)
        sim.run(23.4)
        self.assertEqual(sim.get_current_time(), 33.5)
    
    def test_time_step(self):
        sim.setup(0.123, min_delay=0.246)
        self.assertEqual(sim.get_time_step(), 0.123)
    
    def test_min_delay(self):
        sim.setup(0.123, min_delay=0.246)
        self.assertEqual(sim.get_min_delay(), 0.246)
    
    def test_max_delay(self):
        sim.setup(max_delay=9.87)
        self.assertEqual(sim.get_max_delay(), 9.87)

    def test_callbacks(self):
        total_time = 100.
        callback_steps = [10., 10., 20., 25.]

        # callbacks are called at 0. and after every step
        expected_callcount = [11, 11, 6, 5]
        num_callbacks = len(callback_steps)
        callback_callcount = [0] * num_callbacks

        def make_callback(idx):
            def callback(time):
                callback_callcount[idx] += 1
                return time + callback_steps[idx]
            return callback

        callbacks = [make_callback(i) for i in range(num_callbacks)]
        sim.setup(timestep=0.1, min_delay=0.1)
        sim.run_until(total_time, callbacks=callbacks)

        self.assertTrue(all(callback_callcount[i] == expected_callcount[i]
            for i in range(num_callbacks)))
    
    @unittest.skipUnless(MPI, "test requires mpi4py")
    def test_num_processes(self):
        self.assertEqual(sim.num_processes(), mpi_comm.size)
    
    @unittest.skipUnless(MPI, "test requires mpi4py")
    def test_rank(self):
        self.assertEqual(sim.rank(), mpi_comm.rank)


if __name__ == '__main__':
    unittest.main()
