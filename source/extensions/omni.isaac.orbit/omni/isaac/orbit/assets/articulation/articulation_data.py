# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import torch
from dataclasses import dataclass
from typing import List

from ..rigid_object import RigidObjectData


@dataclass
class ArticulationData(RigidObjectData):
    """Data container for an articulation."""

    ##
    # Properties.
    ##

    joint_names: List[str] = None
    """Joint names in the order parsed by the simulation view."""

    ##
    # Default states.
    ##

    default_joint_pos: torch.Tensor = None
    """Default joint positions of all joints. Shape is ``(count, num_joints)``."""

    default_joint_vel: torch.Tensor = None
    """Default joint velocities of all joints. Shape is ``(count, num_joints)``."""

    ##
    # Joint states <- From simulation.
    ##

    joint_pos: torch.Tensor = None
    """Joint positions of all joints. Shape is ``(count, num_joints)``."""

    joint_vel: torch.Tensor = None
    """Joint velocities of all joints. Shape is ``(count, num_joints)``."""

    joint_acc: torch.Tensor = None
    """Joint acceleration of all joints. Shape is ``(count, num_joints)``."""

    ##
    # Joint commands -- Set into simulation.
    ##

    joint_pos_target: torch.Tensor = None
    """Joint position targets provided to simulation. Shape is ``(count, num_joints)``."""

    joint_vel_target: torch.Tensor = None
    """Joint velocity targets provided to simulation. Shape is ``(count, num_joints)``."""

    joint_effort_target: torch.Tensor = None
    """Joint effort targets provided to simulation. Shape is ``(count, num_joints)``."""

    joint_stiffness: torch.Tensor = None
    """Joint stiffness provided to simulation. Shape is ``(count, num_joints)``."""

    joint_damping: torch.Tensor = None
    """Joint damping provided to simulation. Shape is ``(count, num_joints)``."""

    ##
    # Joint commands -- Explicit actuators.
    ##

    computed_torque: torch.Tensor = None
    """Joint torques computed from the actuator model (before clipping).
    Shape is ``(count, num_joints)``.

    Note: The torques are zero for implicit actuator models.
    """

    applied_torque: torch.Tensor = None
    """Joint torques applied from the actuator model (after clipping).
    Shape is ``(count, num_joints)``.

    Note: The torques are zero for implicit actuator models.
    """

    ##
    # Other Data.
    ##

    soft_joint_pos_limits: torch.Tensor = None
    """Joint positions limits for all joints. Shape is ``(count, num_joints, 2)``."""

    soft_joint_vel_limits: torch.Tensor = None
    """Joint velocity limits for all joints. Shape is ``(count, num_joints, 2)``."""

    gear_ratio: torch.Tensor = None
    """Gear ratio for relating motor torques to applied Joint torques. Shape is ``(count, num_joints)``."""